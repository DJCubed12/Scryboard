"""Stores the RFID-API ID pairings."""

from typing import Any, Dict
from threading import Lock

from card import Card, MatZone

from event_pusher import sendCardUpdate


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

    def update_observers(self):
        sendCardUpdate(self.get_all_jsonable())

    # ----- READ OPERATIONS -----

    def get_card(self, rfid: str) -> Card | None:
        with self._lock:
            return self._cards.get(rfid)

    def get_all(self) -> list[Card]:
        with self._lock:
            return [card for card in self._cards.values()]

    def get_all_jsonable(self) -> list[dict[str, Any]]:
        with self._lock:
            return [card.toJSON() for card in self._cards.values()]

    def get_mats(self) -> list[str]:
        """Get a list of all mat IDs."""
        mats = []
        with self._lock:
            for card in self._cards.values():
                if card.mat_id not in mats:
                    mats.append(card.mat_id)
        return mats

    # ----- CREATE OPERATIONS -----

    def add_card(
        self,
        rfid: str,
        mat_id: str,
        zone: MatZone = MatZone.NOT_PRESENT,
        *,
        api_id: str | None = None
    ) -> None:
        """Raises ValueError if given RFID already exists."""
        with self._lock:
            if rfid in self._cards:
                raise ValueError()
            else:
                self._cards[rfid] = Card(rfid, mat_id, zone, api_id=api_id)
        self.update_observers()

    def bulk_add(self, card_dict: dict[str, Card]) -> None:
        """card_dict is expected to be keyed by the card's RFID. Note: Will overwrite pre-existing cards with the same RFID."""
        with self._lock:
            self._cards.update(card_dict)
        self.update_observers()

    # ----- DELETE OPERATIONS -----

    def remove_card(self, rfid: str) -> bool:
        """Raises KeyError if no card with given rfid was found."""
        with self._lock:
            self._cards.pop(rfid)
        self.update_observers()

    def clear(self) -> None:
        with self._lock:
            self._cards.clear()
        self.update_observers()

    # ----- UPDATE OPERATIONS -----

    def set_zone(self, rfid: str, zone: MatZone):
        """Raises KeyError if no card with given rfid was found."""
        with self._lock:
            self._cards[rfid].zone = zone
        self.update_observers()

    def set_API_ID(self, rfid: str, api_id: str) -> None:
        """Raises KeyError if no card with given rfid was found."""
        with self._lock:
            self._cards[rfid].api_id = api_id
        self.update_observers()

    def set_images(
        self, rfid: str, front_image: str | None, back_image: str | None
    ) -> None:
        """Raises KeyError if no card with given rfid was found. Only updates image if value is given (None will not delete existing image)."""
        with self._lock:
            if front_image:
                self._cards[rfid].front_image = front_image
            if back_image:
                self._cards[rfid].back_image = back_image
        self.update_observers()

    def flip_card(self, rfid: str, to_face_up: bool):
        """Raises KeyError if no card with given rfid was found."""
        with self._lock:
            self._cards[rfid].is_face_up = to_face_up
        self.update_observers()


card_repository = CardRepository()
