from typing import Any
from enum import Enum


class MatZone(Enum):
    """Convert character value into this enum with `MatZone(char)`. Raises ValueError if invalid option."""

    BATTLEFIELD = "B"
    COMMAND = "C"
    LIBRARY = "L"
    GRAVEYARD = "G"
    EXILE = "E"


class Card:
    """A cards API ID along with the mat it was played to. CONSIDER THIS IMMUTABLE; only CardRepository should directly change its values.

    Instance Variables
    ------------------
    rfid: str
    mat_id: str
    api_id: str | None
    is_face_up: boolean - Default is False
    front_image: str | None
    back_image: str | None
    zone: MatZone | None - None implies that the card is known (possibly has been paired), but not yet present on the mat
    """

    def __init__(
        self,
        rfid: str,
        mat_id: str,
        zone: MatZone | None = None,
        *,
        api_id: str | None = None,
    ):
        self.rfid: str = rfid
        self.mat_id: str = mat_id
        self.zone = None
        self.api_id: str | None = api_id
        """None if the frontend hasn't provided an API ID yet"""

        self.is_face_up = False
        self.front_image = None
        self.back_image = None

    def toJSON(self) -> dict[str, Any]:
        return {
            "rfid": self.rfid,
            "mat_id": self.mat_id,
            "api_id": self.api_id,
            "is_face_up": self.is_face_up,
            "front_image": self.front_image,
            "back_image": self.back_image,
            "zone": self.zone.value if self.zone else None,
        }
