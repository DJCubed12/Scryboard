from flask import current_app, request

from repository import card_repository
from card import MatZone


@current_app.post("/rfid")
def post_rfid():
    data = request.json
    print("New RFID post:", data)

    try:
        rfid = data["rfid"]
        mat_id = data["mat_id"]
    except KeyError:
        return {
            "success": False,
            "message": "Must provide rfid and mat_id fields.",
        }, 400

    try:
        card_repository.add_card(rfid, mat_id)
        return {"success": True, "rfid": rfid, "mat_id": mat_id}
    except ValueError as e:
        return {
            "success": False,
            "message": f"Card with rfid={rfid} already added",
        }, 400


@current_app.patch("/card/<rfid>/zone")
def set_zone(rfid: str):
    data = request.json
    try:
        if data["zone"] is not None:
            zone = MatZone(data["zone"])
        else:
            zone = None
    except (KeyError, ValueError):
        return {
            "success": False,
            "message": "zone field must be provided as either 'B', 'C', 'L', 'G', 'E' or null.",
        }, 400

    try:
        card_repository.set_zone(rfid, zone)
        return {
            "success": True,
            "rfid": rfid,
            "zone": zone.value if zone is not None else None,
        }
    except KeyError as e:
        return {
            "success": False,
            "message": f"Card with rfid={rfid} not found",
        }, 404
