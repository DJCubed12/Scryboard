import pytest
from pytest_bdd import given, when, then, scenarios, parsers

from .repository_fixture import repository, CardRepository
from .tools import get_rand_id

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
    context["repo"].add_card(get_rand_id(), get_rand_id())


@when("a card is added with duplicate RFID")
def step_add_card_dup_rfid(context):
    repo: CardRepository = context["repo"]
    rfid = repo.get_all()[0].rfid
    try:
        repo.add_card(rfid, get_rand_id())
    except Exception as e:
        context["error"] = e


@then(parsers.parse("there is {n:d} cards in the repository"))
def step_check_card_count(context, n: int):
    cards = context["repo"].get_all()
    assert len(cards) == n


@then("an error is thrown")
def step_check_for_error(context):
    assert "error" in context
