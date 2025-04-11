from flask import current_app, request

from repository import CardRepository


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
        CardRepository().add_card(rfid, mat_id)
        return {"success": True, "rfid": rfid, "mat_id": mat_id}
    except ValueError as e:
        return {
            "success": False,
            "message": f"Card with rfid={rfid} already added",
        }, 400
