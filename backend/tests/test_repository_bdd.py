import pytest
from pytest_bdd import given, when, then, scenarios, parsers

import os
import sys

from .repository_fixture import repository, CardRepository
from .tools import get_rand_id

# Sets the path to backend/ so all the imports will work
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from card import Card, MatZone

# Link the feature files
scenarios(
    "features/repo.create.feature",
    "features/repo.update.feature",
)


@pytest.fixture
def context():
    return {}


@given("there is an empty repository")
def step_empty_repo(context, repository: CardRepository):
    context["repo"] = repository


@given("there is an non-empty repository")
def step_nonempty_repo(context, repository: CardRepository):
    mat1 = get_rand_id()
    mat2 = get_rand_id()
    repository.add_card(get_rand_id(), mat1)
    repository.add_card(get_rand_id(), mat1)
    repository.add_card(get_rand_id(), mat1)
    repository.add_card(get_rand_id(), mat2)
    repository.add_card(get_rand_id(), mat2)
    context["repo"] = repository


@when("a card is added")
def step_add_card(context):
    rfid = get_rand_id()
    context["repo"].add_card(rfid, get_rand_id())
    context["added-rfid"] = get_rand_id()


@when("a card is added with duplicate RFID")
def step_add_card_dup_rfid(context):
    repo: CardRepository = context["repo"]
    rfid = repo.get_all()[0].rfid
    try:
        repo.add_card(rfid, get_rand_id())
    except Exception as e:
        context["error"] = e


@when(parsers.parse("a card is added with zone {zone}"))
def step_add_card_with_zone(context, zone: str):
    matZone = MatZone(zone)
    rfid = get_rand_id()
    context["repo"].add_card(rfid, get_rand_id(), zone=matZone)
    context["selected-card"] = rfid


@when(parsers.parse("I select a card"))
def step_select_card(context):
    card = context["repo"].get_all()[0]
    context["selected-card"] = card.rfid


@when(parsers.parse("set its zone to {zone}"))
def step_update_property(context, zone: str):
    repo: CardRepository = context["repo"]
    rfid = context["selected-card"]
    repo.set_zone(rfid, MatZone(zone))


@when("set its API ID")
def step_set_api_id(context):
    repo: CardRepository = context["repo"]
    api_id = get_rand_id()
    repo.set_API_ID(context["selected-card"], api_id)
    context["api-id"] = api_id


@when(parsers.parse("I flip the card face {up_or_down}"))
def step_flip_card(context, up_or_down: str):
    to_face_up = up_or_down == "up"
    context["repo"].flip_card(context["selected-card"], to_face_up)


@when(parsers.parse("I set the {front_or_back} image"))
def step_set_one_image(context, front_or_back: str):
    set_front = front_or_back == "front"
    rfid = context["selected-card"]
    if set_front:
        context["repo"].set_images(rfid, "test", None)
    else:
        context["repo"].set_images(rfid, None, "test")


@when("I set both images")
def step_set_one_image(context):
    rfid = context["selected-card"]
    context["repo"].set_images(rfid, "test_front", "test_back")


@then(parsers.parse("there is {n:d} cards in the repository"))
def step_check_card_count(context, n: int):
    cards = context["repo"].get_all()
    assert len(cards) == n


@then(parsers.parse("the card has zone {zone}"))
def step_check_card_zone(context, zone: str):
    matZone = MatZone(zone)
    card: Card = context["repo"].get_card(context["selected-card"])
    assert card.zone == matZone


@then(parsers.parse("the card is face {up_or_down}"))
def step_check_face_up_or_down(context, up_or_down: str):
    card: Card = context["repo"].get_card(context["selected-card"])
    assert card.is_face_up == (up_or_down == "up")


@then(parsers.parse("the card's {front_or_back} image is set"))
def step_image_is_set(context, front_or_back: str):
    card: Card = context["repo"].get_card(context["selected-card"])
    if front_or_back == "front":
        assert card.front_image is not None
    else:
        assert card.back_image is not None


@then(parsers.parse("the card's {front_or_back} image is not set"))
def step_image_is_set(context, front_or_back: str):
    card: Card = context["repo"].get_card(context["selected-card"])
    if front_or_back == "front":
        assert card.front_image is None
    else:
        assert card.back_image is None


@then("the card has the given API ID")
def step_check_api_id(context):
    card: Card = context["repo"].get_card(context["selected-card"])
    assert card.api_id == context["api-id"]


@then("an error is thrown")
def step_check_for_error(context):
    assert "error" in context
