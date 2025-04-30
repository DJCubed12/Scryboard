"""Endpoints relating to changing cards."""

from flask import current_app, request

from repository import card_repository
from card import MatZone


@current_app.patch("/card/<rfid>/pair")
def pair_card(rfid: str):
    data = request.json
    print(f"Patch for card RFID#{rfid}:", data)

    try:
        api_id = data["api_id"]
    except KeyError:
        return {
            "success": False,
            "message": "Must provide an api_id field.",
        }, 400

    # Get card image URLs, if provided
    try:
        front_image: str | None = data["front_image"]
    except KeyError:
        front_image = None
    try:
        back_image: str | None = data["back_image"]
    except KeyError:
        back_image = None

    try:
        card_repository.set_API_ID(rfid, api_id)
        if front_image or back_image:
            card_repository.set_images(rfid, front_image, back_image)

        return {"success": True, "rfid": rfid, "api_id": api_id}
    except KeyError as e:
        return {
            "success": False,
            "message": f"No card with rfid={rfid}",
        }, 404


@current_app.patch("/card/<rfid>/flip")
def flip_card(rfid: str):
    data = request.json
    try:
        to_face_up: bool = data["to_face_up"]
    except (KeyError, ValueError):
        return {
            "success": False,
            "message": "'to_face_up' boolean field missing",
        }, 400

    try:
        card_repository.flip_card(rfid, to_face_up)
        return {
            "success": True,
            "rfid": rfid,
            "is_face_up": to_face_up,
        }
    except KeyError as e:
        return {
            "success": False,
            "message": f"Card with rfid={rfid} not found",
        }, 404


@current_app.patch("/card/<rfid>/zone")
def set_zone(rfid: str):
    data = request.json
    try:
        if data["zone"] is not None:
            zone = MatZone(data["zone"])
        else:
            zone = None
    except (KeyError, ValueError):
        return {
            "success": False,
            "message": "zone field must be provided as either 'B', 'C', 'L', 'G', 'E' or null.",
        }, 400

    try:
        card_repository.set_zone(rfid, zone)
        return {
            "success": True,
            "rfid": rfid,
            "zone": zone.value if zone is not None else None,
        }
    except KeyError as e:
        return {
            "success": False,
            "message": f"Card with rfid={rfid} not found",
        }, 404
