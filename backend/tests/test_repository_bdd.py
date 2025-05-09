import pytest
from pytest_bdd import given, when, then, scenarios, parsers

from .repository_fixture import repository, CardRepository

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


@when("a card is added")
def step_add_card(context):
    context["repo"].add_card("test_rfid", "test_mat_id")


@then(parsers.parse("there is {n:d} cards in the repository"))
def step_check_card_count(context, n: int):
    cards = context["repo"].get_all()
    assert len(cards) == n
