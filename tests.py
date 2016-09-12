import pytest
import pytest_flask
from flask import url_for
import json

from api import create_app
from api.models import db, Page, Wikipage


@pytest.fixture(scope="module")
def app():
    app = create_app()
    db.init_app(app)
    with app.app_context():
        db.drop_all(bind=None, )
        db.create_all()
        w1 = Wikipage()
        p11 = Page(title="first title", text="s", wikipage=w1)
        p12 = Page(title="first title2", text="ss", wikipage=w1)
        w1.current_page = p12

        w2 = Wikipage()
        p2 = Page(title="first title of second wiki", text="z", wikipage=w2)
        w2.current_page = p2

        db.session.add_all([w1, w2, p11, p12, p2])
        db.session.commit()
    yield app


def test_all_response(client):
    res = client.get(url_for('main.all'))
    assert res.json == ([
      {
        "current_page_id": 1,
        "id": 1
      },
      {
        "current_page_id": 2,
        "id": 2
      }
    ])

def test_versions_response(client):
    res = client.get(url_for('main.versions', wiki_id=1))
    assert res.json == [
        {
            "id": 1,
            "text": "ss",
            "title": "first title2",
            "wikipage_id": 1
        },
        {
            "id": 3,
            "text": "s",
            "title": "first title",
            "wikipage_id": 1
        }
    ]

def test_distinct_response(client):
    res = client.get(url_for('main.distinct', page_id=1))
    assert res.json == {
      "id": 1,
      "text": "ss",
      "title": "first title2",
      "wikipage_id": 1
    }


def test_current_response(client):
    res = client.get(url_for('main.current', wiki_id=1))
    assert res.json == {
      "id": 1,
      "text": "ss",
      "title": "first title2",
      "wikipage_id": 1
    }

def test_add_new(client):
    res = client.post(url_for('main.add_new', wiki_id=2), data={'title': "New", 'text': "yay"}, headers={'mimetype': 'application/json'})
    assert res.json == {
      "status": 200
    }
    res = client.get(url_for('main.current', wiki_id=2))
    assert res.json == {
      "id": 4,
      "text": "yay",
      "title": "New",
      "wikipage_id": 2
    }


def test_set_current(client):
    res = client.post(url_for('main.set_current', wiki_id=2), data={'page_id': 2}, headers={'mimetype': 'application/json'})
    assert res.json == {
      "status": 200
    }
    res = client.get(url_for('main.current', wiki_id=2))
    assert res.json == {
  "id": 2,
  "text": "z",
  "title": "first title of second wiki",
  "wikipage_id": 2
}

