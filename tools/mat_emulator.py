import requests, random

backend_url = "http://localhost:5000/rfid"

rand_rfid_tag = random.getrandbits(64)
rfid_object = {'rfid': bytes.hex(rand_rfid_tag.to_bytes(8))}

req = requests.post(backend_url, json = rfid_object)

print(req.text)