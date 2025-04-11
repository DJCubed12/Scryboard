from flask import current_app

from repository import CardRepository


@current_app.get("/cards")
def get_current_board():
    return {"cards": [card.toJSON() for card in CardRepository().get_all()]}
