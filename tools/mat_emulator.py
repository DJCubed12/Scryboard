import requests, random
from tkinter import *
from tkinter import ttk

backend_url = "http://localhost:5000/card"
mat_sent_RFID = dict()


def send_rfid_post(matid, rfid):
    rfid_object = {"mat_id": matid, "rfid": rfid}
    req = requests.post(backend_url, json=rfid_object)
    print(req.text)


def new_mat():
    matid = bytes.hex(random.getrandbits(64).to_bytes(8))
    mat_listbox.insert(END, matid)
    mat_sent_RFID[matid] = []


def send_rand_rfid():
    selection = mat_listbox.curselection()
    if not selection:
        return
    index = selection[0]
    matid = mat_listbox.get(index)
    rfid = bytes.hex(random.getrandbits(64).to_bytes(8))
    mat_sent_RFID[matid].append(rfid)
    rfid_listbox.insert(END, rfid)
    send_rfid_post(matid, rfid)


def resend_rfid():
    matsel = mat_listbox.curselection()
    rfidsel = rfid_listbox.curselection()
    if not matsel or not rfidsel:
        return
    matindex = matsel[0]
    rfidindex = rfidsel[0]
    matid = mat_listbox.get(matindex)
    rfid = rfid_listbox.get(rfidindex)
    send_rfid_post(matid, rfid)


def onselect_rfid(event):
    box = event.widget
    selection = box.curselection()
    if not selection:
        btn_resend_rfid["state"] = DISABLED
    else:
        btn_resend_rfid["state"] = NORMAL


def onselect_mat(event):
    box = event.widget
    selection = box.curselection()
    if not selection:
        return
    index = selection[0]
    matid = box.get(index)
    print("Selected: " + matid)
    btn_new_rfid["state"] = NORMAL
    rfid_listbox.delete(0, END)
    for rfid in mat_sent_RFID[matid]:
        rfid_listbox.insert(END, rfid)


root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

Button(frm, text="Add Mat", command=new_mat).grid(column=0, row=0)

mat_listbox = Listbox(frm, selectmode=SINGLE, exportselection=False)
mat_listbox.grid(column=0, row=1)
mat_listbox.bind("<<ListboxSelect>>", onselect_mat)

rfid_listbox = Listbox(frm, selectmode=SINGLE)
rfid_listbox.grid(column=1, row=1, columnspan=2)
rfid_listbox.bind("<<ListboxSelect>>", onselect_rfid)

btn_new_rfid = Button(
    frm, text="Send Rand RFID", command=send_rand_rfid, state=DISABLED
)
btn_new_rfid.grid(column=1, row=0)

btn_resend_rfid = Button(frm, text="Resend RFID", command=resend_rfid, state=DISABLED)
btn_resend_rfid.grid(column=2, row=0)

root.mainloop()
