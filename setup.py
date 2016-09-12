from flask_sqlalchemy import SQLAlchemy
from flask import Flask

from api.models import Wikipage, Page, db
from config import Config
from api import create_app


app = create_app()
db.init_app(app)

with app.app_context():
    db.create_all()

    p = Page(title="zApp", text="f")
    w = Wikipage()
    w.current_page = p
    p.wikipage = w

    db.session.add(w)
    db.session.commit()