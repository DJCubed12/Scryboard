"""Stores the RFID-API ID pairings."""

from typing import Dict
from threading import Lock


class IdPairingRepository:
    """Singleton repository for card RFID-API ID pairings."""

    _instance = None
    _lock = Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(IdPairingRepository, cls).__new__(cls)
                cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        with self._lock:
            if self._initialized:
                return
            self._initialized = True

            self._pairings: Dict[int, int] = {}
            """Dictionary with RFID index, API ID values."""

    def get_API_Id(self, rfid: int) -> int | None:
        with self._lock:
            return self._pairings.get(rfid)

    def add_pair(self, rfid, api_id) -> None:
        """Raises ValueError if given RFID already exists."""
        with self._lock:
            if rfid in self._pairings:
                raise ValueError()
            else:
                self._pairings[rfid] = api_id

    def remove_pair(self, rfid) -> bool:
        """Returns True if rfid existed and was successfully deleted."""
        with self._lock:
            if rfid in self._pairings:
                self._pairings.pop(rfid)
                return True
            else:
                return False

    def clear(self) -> None:
        with self._lock:
            self._pairings.clear()
