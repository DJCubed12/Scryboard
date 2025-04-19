"""Endpoints for import/exporting cards from the repository."""

import json

from flask import Response, current_app

from repository import card_repository


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
