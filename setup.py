from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import ForeignKeyConstraint

from api.models import Wikipage, Page, db
from config import Config
from api import create_app


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