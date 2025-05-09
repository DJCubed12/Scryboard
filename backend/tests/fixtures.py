import pytest

import os
import sys


# Sets the path to backend/ so all the imports will work
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from repository import CardRepository
from app import create_app


@pytest.fixture
def repository():
    CardRepository._instance = None
    yield CardRepository()


@pytest.fixture
def flask_api():
    app = create_app()
    app.config["TESTING"] = True
    with app.app_context():
        with app.test_client() as client:
            yield client
