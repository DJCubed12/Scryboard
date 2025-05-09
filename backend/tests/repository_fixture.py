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
