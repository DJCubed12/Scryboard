"""Endpoints for import/exporting cards from the repository."""

import json

from flask import Response, current_app, request

from repository import card_repository
from .frontend_endpoints import get_current_board


@current_app.get("/cards/export")
def export_all():
    cards = card_repository.get_all_jsonable()
    return Response(
        json.dumps(cards),
        mimetype="application/json",
        headers={"Content-Disposition": "attachment;filename=scryboard-export.json"},
    )


@current_app.get("/cards/<mat_id>/export")
def export(mat_id: str):
    cards = [
        card
        for card in card_repository.get_all_jsonable()
        if card.get("mat_id") == mat_id
    ]

    print(f"Found {len(cards)} cards tied to mat {mat_id}")
    if len(cards) == 0:
        return {"message": f"No mats with id {mat_id}."}, 404

    return Response(
        json.dumps(cards),
        mimetype="application/json",
        headers={"Content-Disposition": "attachment;filename=scryboard-export.json"},
    )


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
        card_repository.import_cards(cards_json_data)
    except KeyError as e:
        return {"message": str(e).replace('"', "")}, 400

    return get_current_board()
