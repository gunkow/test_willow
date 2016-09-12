from flask import Blueprint, jsonify
from .models import db, Wikipage, Page


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

@main.route('/<int:page_id>')
def versions(page_id):
    page = Page.query.get(page_id)
    return jsonify(page.asdict())

@main.route('/<int:wiki_id>/current')
def versions(wiki_id):
    wiki = Wikipage.query.get(wiki_id)
    current_page = wiki.current_page
    return jsonify(current_page.asdict())



