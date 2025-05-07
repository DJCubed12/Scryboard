import requests, random, json
from tkinter import *
from tkinter import ttk

backend_url = "http://localhost:5000"
mats = dict()

ALL_ZONES = ['Battlefield', 'Command', 'Library', 'Graveyard', 'Exile', 'Not Specified']


# def send_rfid_post(matid, rfid):
#     rfid_object = {"mat_id": matid, "rfid": rfid}
#     req = requests.post(backend_url, json=rfid_object)
#     print(req.text)


def send_full_post(matid):
    backend_replace_mat = (backend_url + "/cards/<mat_id>/replace").replace("<mat_id>", matid)
    json_object = []
    for zone in mats[matid]:
        for rfid in zone:
            json_object.append({'rfid': rfid, 'mat_id': matid, 'zone': ALL_ZONES[mats[matid].index(zone)][0]}) #[[rfid, matid, ALL_ZONES[mats[matid].index(zone)][0]]]
    req = requests.post(backend_replace_mat, json=json_object)
    print(req.text)


def new_mat():
    matid = bytes.hex(random.getrandbits(64).to_bytes(8))
    mat_listbox.insert(END, matid)
    mats[matid] = [[] for zone in ALL_ZONES]


def get_zone_rfid_string(zone_index, rfid):
    return f"{ALL_ZONES[zone_index][0]}: {rfid}"


def strip_zone_string(zone_rfid_string):
    return zone_rfid_string.split(": ")[1]


def add_rand_rfid():
    add_rfid(bytes.hex(random.getrandbits(64).to_bytes(8)))
    refresh_rfid()


def add_rfid(rfid):
    matsel = mat_listbox.curselection()
    if not matsel:
        return
    matid = mat_listbox.get(matsel[0])
    zone = val_zone_index.get()
    mats[matid][zone].append(rfid)


def remove_rfid():
    matsel = mat_listbox.curselection()
    rfidsel = rfid_listbox.curselection()
    if not matsel or not rfidsel:
        return
    matid = mat_listbox.get(matsel[0])
    for rfid in rfidsel: 
        rfid_to_remove = strip_zone_string(rfid_listbox.get(rfid))
        for zone in range(len(ALL_ZONES)):
            if rfid_to_remove in mats[matid][zone]:
                mats[matid][zone].remove(rfid_to_remove)
    for index, rfid in enumerate(rfidsel):
        rfid_listbox.delete(rfid - index)
    btn_rem_rfid["state"] = DISABLED


def send_post():
    matsel = mat_listbox.curselection()
    if not matsel:
        return
    matid = mat_listbox.get(matsel[0])
    send_full_post(matid)


def onselect_rfid(event):
    rfidsel = rfid_listbox.curselection()
    if not rfidsel:
        btn_rem_rfid["state"] = DISABLED
    else:
        btn_rem_rfid["state"] = NORMAL


def refresh_rfid():
    matsel = mat_listbox.curselection()
    if not matsel:
        return
    matid = mat_listbox.get(matsel[0])
    rfid_listbox.delete(0, END)
    for zone_index, zone in enumerate(mats[matid]):
        for rfid in zone:
            rfid_listbox.insert(END, get_zone_rfid_string(zone_index, rfid))

def onselect_zone(event):
    refresh_rfid()
    
def onselect_mat(event):
    btn_new_rfid["state"] = NORMAL
    refresh_rfid()

def zone_change():
    matsel = mat_listbox.curselection()
    rfidsel = rfid_listbox.curselection()
    if not matsel or not rfidsel:
        return
    matid = mat_listbox.get(matsel[0])
    rfid_to_move = []
    for rfid in rfidsel: 
        rfid_to_remove = strip_zone_string(rfid_listbox.get(rfid))
        rfid_to_move.append(rfid_to_remove)
        for zone in range(len(ALL_ZONES)):
            if rfid_to_remove in mats[matid][zone]:
                mats[matid][zone].remove(rfid_to_remove)
    for rfid in rfid_to_move:
        add_rfid(rfid)
    refresh_rfid()


root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

Button(frm, text="Add Mat", command=new_mat).grid(column=0, row=0)

mat_listbox = Listbox(frm, selectmode=SINGLE, exportselection=False)
mat_listbox.grid(column=0, row=1)
mat_listbox.bind("<<ListboxSelect>>", onselect_mat)

rfid_listbox = Listbox(frm, selectmode=MULTIPLE)
rfid_listbox.grid(column=2, row=1, columnspan=2)
rfid_listbox.bind("<<ListboxSelect>>", onselect_rfid)

btn_new_rfid = Button(frm, text="Add RFID", command=add_rand_rfid, state=DISABLED)
btn_new_rfid.grid(column=2, row=0)

btn_rem_rfid = Button(frm, text="Rem RFID", command=remove_rfid, state=DISABLED)
btn_rem_rfid.grid(column=3, row=0)

btn_send_post = Button(frm, text="Send Mat RFIDs", command=send_post)
btn_send_post.grid(column=2, row=2, columnspan=2)

val_zone_index = IntVar(root, 0)
rdo_zones = []
rdo_frm = ttk.Frame(frm, padding=10)
rdo_frm.grid(column=1, row=1)

for index, zone in enumerate(ALL_ZONES):
    rdo_zones.append(Radiobutton(rdo_frm, text=zone, variable=val_zone_index, value=index, command=zone_change))
    rdo_zones[index].grid(column=0, row=index, sticky='w')


root.mainloop()
