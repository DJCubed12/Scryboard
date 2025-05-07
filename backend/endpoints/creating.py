"""Endpoints related to card creation."""

from flask import current_app, request

import json

from repository import card_repository, MatZone
from card_import_service import card_import_service
from .reading import get_all_cards


@current_app.post("/card")
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


@current_app.post("/cards/<mat_id>/replace")
def replace_mat(mat_id: str):
    """Adds or updates existing RFIDs in the database, then responds with the current card list."""
    new_cards = [card_obj for card_obj in request.json]
    repo_cards = card_repository.get_all()
    repo_rfids = [card.rfid for card in repo_cards]

    try:
        for card in new_cards:
            if card['rfid'] in repo_rfids:
                card_repository.set_zone(card['rfid'], MatZone(card['zone']))
            else: 
                card_repository.add_card(card['rfid'], card['mat_id'], zone=MatZone(card['zone']))
    except KeyError:
        return {
            "success": False,
            "message": f"Test!",
        }, 400
    
    return get_all_cards()
    

@current_app.post("/cards/import")
def import_cards():
    """Imports cards from the 'importFile' file in post form data, then responds with the current card list."""

    try:
        file = request.files["importFile"]
    except KeyError:
        return {
            "message": "Missing file for importing cards. Upload a JSON file under 'importFile'"
        }, 400

    if file.content_type != "application/json":
        return {"message": "Imported file must be in JSON format"}, 400

    cards_json_data = json.loads(file.stream.read())
    print(f"Importing {len(cards_json_data)} cards...")
    try:
        card_import_service.import_cards(cards_json_data)
    except KeyError as e:
        return {"message": str(e).replace('"', "")}, 400

    return get_all_cards()
