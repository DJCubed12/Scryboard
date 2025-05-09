import pytest
from pytest_mock import MockFixture

import os
import sys


# Sets the path to backend/ so all the imports will work
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from repository import CardRepository


@pytest.fixture
def repository(mocker: MockFixture):
    with mocker.patch("repository.sendCardUpdate"):
        with mocker.patch("repository.sendMatUpdate"):
            CardRepository._instance = None
            yield CardRepository()


def test_is_empty(repository: CardRepository):
    assert repository.get_all() == []


def test_add_card(repository: CardRepository):
    repository.add_card("test", "test")
    assert len(repository.get_all()) == 1


def test_still_empty(repository: CardRepository):
    assert repository.get_all() == []
