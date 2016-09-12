import pytest
import pytest_flask
from flask import url_for

from api import create_app




@pytest.fixture
def app():
    app = create_app()
    return app


def test_my_json_response(client):
    res = client.get(url_for('main.hello_world'))
    assert res.json == 42