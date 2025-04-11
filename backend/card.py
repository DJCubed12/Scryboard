from typing import Any


class Card:
    """A cards API ID along with the mat it was played to. CONSIDER THIS IMMUTABLE; only CardRepository should directly change its values."""

    def __init__(self, mat_id: int, api_id: str | None = None):
        self.mat_id: int = mat_id
        self.api_id: str | None = api_id
        """None if the frontend hasn't provided an API ID yet"""

    def toJSON(self) -> dict[str, Any]:
        return {"mat_id": self.mat_id, "api_id": self.api_id}
