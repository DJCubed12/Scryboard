import pytest

from .repository_fixture import repository, CardRepository


def test_is_empty(repository: CardRepository):
    assert repository.get_all() == []


def test_add_card(repository: CardRepository):
    repository.add_card("test", "test")
    assert len(repository.get_all()) == 1


def test_still_empty(repository: CardRepository):
    assert repository.get_all() == []
