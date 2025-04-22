from typing import Any

from card import Card, MatZone
from repository import CardRepository


class CardImportService:
    def __init__(self):
        self.card_repository = CardRepository()

    def import_cards(self, cards_from_json: list[dict[str, Any]]):
        """Add cards from cards_from_json to repository, overwriting existing ones in the case of conflict.
        Raises KeyError if cards have invalid format (no cards will be added in this case). cards_from_json should be the direct output of json.decode; a list of dictionaries with at least 'rfid', 'mat_id', and 'api_id' (can be null/None) fields.
        """
        new_cards: dict[str, Card] = dict()
        for card in cards_from_json:
            # Raises KeyError if these three fields are not supplied
            rfid = card["rfid"]
            mat_id = card["mat_id"]
            api_id = card["api_id"]
            new_card = Card(rfid, mat_id, api_id=api_id)

            zone = card.get("zone")
            if zone:
                new_card.zone = MatZone(zone)
            new_card.is_face_up = card.get("is_face_up", False)
            # SECURITY ISSUE: These image URLs are interpolated directly into HTML, maybe check/scrub them before importing?
            # These default to None if not available
            new_card.front_image = card.get("front_image")
            new_card.back_image = card.get("back_image")

            new_cards[rfid] = new_card

        # Note: Will overwrite existing cards with same RFID
        self.card_repository.bulk_add(new_cards)


card_import_service = CardImportService()
