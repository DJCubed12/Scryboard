import requests, random

backend_url = "http://localhost:5000/rfid"

rfid_object = {'rfid': bytes.hex(random.getrandbits(64).to_bytes(8)),
               'matid': bytes.hex(random.getrandbits(64).to_bytes(8))
}

req = requests.post(backend_url, json = rfid_object)

print(req.text)