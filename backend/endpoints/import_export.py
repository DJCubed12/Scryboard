"""Endpoints for import/exporting cards from the repository."""

import json

from flask import Response, current_app

from repository import CardRepository


@current_app.get("/file")
def export():
    cards = [card.toJSON() for card in CardRepository().get_all()]
    return Response(
        json.dumps(cards),
        mimetype="application/json",
        headers={"Content-Disposition": "attachment;filename=cards.json"},
    )
