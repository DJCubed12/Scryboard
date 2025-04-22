"""Stores the RFID-API ID pairings."""

from typing import Any, Dict
from threading import Lock

from card import Card, MatZone


class CardRepository:
    """Singleton repository for mapping RFIDs to Card objects."""

    _instance = None
    _lock = Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(CardRepository, cls).__new__(cls)
                cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        with self._lock:
            if self._initialized:
                return
            self._initialized = True

            self._cards: Dict[int, Card] = {}
            """Dictionary with RFID index and Card values."""

    def get_card(self, rfid: str) -> Card | None:
        with self._lock:
            return self._cards.get(rfid)

    def get_all(self) -> list[Card]:
        with self._lock:
            return [card for card in self._cards.values()]

    def get_all_jsonable(self) -> list[dict[str, Any]]:
        with self._lock:
            return [card.toJSON() for card in self._cards.values()]

    def add_card(
        self,
        rfid: str,
        mat_id: str,
        zone: MatZone | None = None,
        *,
        api_id: str | None = None
    ) -> None:
        """Raises ValueError if given RFID already exists."""
        with self._lock:
            if rfid in self._cards:
                raise ValueError()
            else:
                self._cards[rfid] = Card(rfid, mat_id, zone, api_id=api_id)

    def bulk_add(self, card_dict: dict[str, Card]) -> None:
        """card_dict is expected to be keyed by the card's RFID. Note: Will overwrite pre-existing cards with the same RFID."""
        with self._lock:
            self._cards.update(card_dict)

    def remove_card(self, rfid: str) -> bool:
        """Returns True if rfid existed and was successfully deleted."""
        with self._lock:
            if rfid in self._cards:
                self._cards.pop(rfid)
                return True
            else:
                return False

    def clear(self) -> None:
        with self._lock:
            self._cards.clear()

    def set_API_ID(self, rfid: str, api_id: str) -> None:
        """Raises KeyError if no card with given rfid was found."""
        with self._lock:
            self._cards[rfid].api_id = api_id


card_repository = CardRepository()
