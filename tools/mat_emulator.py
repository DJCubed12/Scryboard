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
            json_object += {"rfid": rfid, "mat_id": matid, "zone": zone}
    req = requests.post(backend_replace_mat, json=json_object)
    print(req.text)


def new_mat():
    matid = bytes.hex(random.getrandbits(64).to_bytes(8))
    mat_listbox.insert(END, matid)
    mats[matid] = [[] for zone in ALL_ZONES]


def add_rand_rfid():
    matsel = mat_listbox.curselection()
    zonesel = zone_listbox.curselection()
    if not matsel or not zonesel:
        return
    matid = mat_listbox.get(matsel[0])
    zone = zone_listbox.get(zonesel[0])
    rfid = bytes.hex(random.getrandbits(64).to_bytes(8))
    mats[matid][ALL_ZONES.index(zone)].append(rfid)
    rfid_listbox.insert(END, rfid)


def remove_rfid():
    matsel = mat_listbox.curselection()
    zonesel = zone_listbox.curselection()
    rfidsel = rfid_listbox.curselection()
    if not matsel or not zonesel or not rfidsel:
        return
    matid = mat_listbox.get(matsel[0])
    zone = zone_listbox.get(zonesel[0])
    rfid = rfid_listbox.get(rfidsel[0])
    mats[matid][ALL_ZONES.index(zone)].remove(rfid)
    rfid_listbox.delete(rfidsel)
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
    zonesel = zone_listbox.curselection()
    if not matsel or not zonesel:
        return
    matid = mat_listbox.get(matsel[0])
    zone = zone_listbox.get(zonesel[0])
    rfid_listbox.delete(0, END)
    for rfid in mats[matid][ALL_ZONES.index(zone)]:
        rfid_listbox.insert(END, rfid)

def onselect_zone(event):
    refresh_rfid()
    
def onselect_mat(event):
    btn_new_rfid["state"] = NORMAL
    refresh_rfid()


root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

Button(frm, text="Add Mat", command=new_mat).grid(column=0, row=0)

mat_listbox = Listbox(frm, selectmode=SINGLE, exportselection=False)
mat_listbox.grid(column=0, row=1)
mat_listbox.bind("<<ListboxSelect>>", onselect_mat)

zone_listbox = Listbox(frm, selectmode=SINGLE, exportselection=False)
zone_listbox.grid(column=1, row=1)
zone_listbox.bind("<<ListboxSelect>>", onselect_zone)
for zone in ALL_ZONES:
    zone_listbox.insert(END, zone)
zone_listbox.select_set(0)

rfid_listbox = Listbox(frm, selectmode=SINGLE)
rfid_listbox.grid(column=2, row=1, columnspan=2)
rfid_listbox.bind("<<ListboxSelect>>", onselect_rfid)

btn_new_rfid = Button(frm, text="Add RFID", command=add_rand_rfid, state=DISABLED)
btn_new_rfid.grid(column=2, row=0)

btn_rem_rfid = Button(frm, text="Rem RFID", command=remove_rfid, state=DISABLED)
btn_rem_rfid.grid(column=3, row=0)

btn_send_post = Button(frm, text="Send Mat RFIDs", command=send_post, state=DISABLED)
btn_send_post.grid(column=2, row=2, columnspan=2)

root.mainloop()
