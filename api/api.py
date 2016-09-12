from flask import Blueprint, jsonify, request
from .models import db, Wikipage, Page
import json


main = Blueprint('main', __name__)


@main.route('/')
def all():
    wikis = Wikipage.query.all()
    return jsonify(map(lambda wiki: wiki.asdict(), wikis))

@main.route('/<int:wiki_id>')
def versions(wiki_id):
    wiki = Wikipage.query.get(wiki_id)
    pages = wiki.pages
    return jsonify(map(lambda page: page.asdict(), pages))

@main.route('/page/<int:page_id>')
def distinct(page_id):
    page = Page.query.get(page_id)
    return jsonify(page.asdict())

@main.route('/<int:wiki_id>/current')
def current(wiki_id):
    wiki = Wikipage.query.get(wiki_id)
    current_page = wiki.current_page
    return jsonify(current_page.asdict())

# EDIT

@main.route('/<int:wiki_id>/', methods=['POST'])
def add_new(wiki_id):
    wiki = Wikipage.query.get(wiki_id)
    data = request.values
    wiki.add_new_page(data)
    return jsonify(status=200)



