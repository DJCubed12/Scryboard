from flask import current_app, request

from repository import CardRepository


@current_app.get("/cards")
def get_current_board():
    return {"cards": [card.toJSON() for card in CardRepository().get_all()]}


@current_app.patch("/card/<rfid>")
def pair_api_id(rfid: int):
    data = request.json
    print(f"Patch for card RFID#{rfid}:", data)

    try:
        api_id = data["api_id"]
    except KeyError:
        return {
            "success": False,
            "message": "Must provide an api_id field.",
        }, 400

    try:
        CardRepository().set_API_ID(rfid, api_id)
        return {"success": True, "rfid": rfid, "api_id": api_id}
    except KeyError as e:
        return {
            "success": False,
            "message": f"No card with rfid={rfid}",
        }, 400
