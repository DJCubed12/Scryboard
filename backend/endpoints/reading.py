"""Endpoints for card read operations."""

import json

from flask import Response, current_app, send_file

from constants import CARD_BACK_DEFAULT
from repository import card_repository


@current_app.get("/mats")
def get_mat_ids():
    return {"mat_ids": card_repository.get_mats()}


@current_app.get("/cards")
def get_all_cards():
    return {"cards": card_repository.get_all_jsonable()}


@current_app.get("/card/<rfid>")
def get_card(rfid: str):
    try:
        return {"card": card_repository.get_card(rfid).toJSON()}
    except KeyError:
        return {
            "success": False,
            "message": f"No card with rfid={rfid}",
        }, 404


@current_app.get("/cards/export")
def export_all():
    cards = card_repository.get_all_jsonable()
    return Response(
        json.dumps(cards),
        mimetype="application/json",
        headers={"Content-Disposition": "attachment;filename=scryboard-export.json"},
    )


@current_app.get("/cards/<mat_id>/export")
def export_mat(mat_id: str):
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


@current_app.get("/default-card-back")
def get_default_card_back():
    return send_file(CARD_BACK_DEFAULT, mimetype="image/jpg")
