import pytest

import os
import sys

from .fixtures import flask_api
from .tools import get_rand_id

# Sets the path to backend/ so all the imports will work
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from card import Card, MatZone
from repository import CardRepository


def test_post_card_success(flask_api):
    rfid = get_rand_id()
    mat_id = get_rand_id()
    data = {"rfid": rfid, "mat_id": mat_id}
    resp = flask_api.post("/card", json=data)

    assert resp.status_code == 200
    assert resp.json["success"] == True
    assert resp.json["rfid"] == rfid
    assert resp.json["mat_id"] == mat_id


# def test_post_card_no_rfid(flask_api):
#     mat_id = get_rand_id()
#     data = {"mat_id": mat_id}
#     resp = flask_api.post("/card", json=data)

#     assert resp.status_code == 400
#     assert resp.json["success"] == False
