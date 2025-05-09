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
    "features/repo.add_card.feature",
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
    context["added-card"] = rfid


@then(parsers.parse("there is {n:d} cards in the repository"))
def step_check_card_count(context, n: int):
    cards = context["repo"].get_all()
    assert len(cards) == n


@then(parsers.parse("the card is in the repository with zone {zone}"))
def step_check_card_zone(context, zone: str):
    matZone = MatZone(zone)
    card: Card = context["repo"].get_card(context["added-card"])
    assert card.zone == matZone


@then(parsers.parse("the card is face {up_or_down}"))
def step_check_face_up_or_down(context, up_or_down: str):
    card: Card = context["repo"].get_card(context["added-card"])
    assert card.is_face_up == (up_or_down == "up")


@then("an error is thrown")
def step_check_for_error(context):
    assert "error" in context
