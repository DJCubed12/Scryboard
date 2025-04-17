from typing import Any


class Card:
    """A cards API ID along with the mat it was played to. CONSIDER THIS IMMUTABLE; only CardRepository should directly change its values."""

    def __init__(self, rfid: str, mat_id: str, api_id: str | None = None):
        self.rfid: str = rfid
        self.mat_id: str = mat_id
        self.api_id: str | None = api_id
        """None if the frontend hasn't provided an API ID yet"""

    def toJSON(self) -> dict[str, Any]:
        return {"rfid": self.rfid, "mat_id": self.mat_id, "api_id": self.api_id}
