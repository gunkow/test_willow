from flask import Blueprint, jsonify
from .models import db, Wikipage, Page


main = Blueprint('main', __name__)


@main.route('/')
def all():
    wikis = Wikipage.query.all()
    return jsonify(map(lambda wiki: wiki.asdict(), wikis))

