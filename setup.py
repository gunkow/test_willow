from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# Create the above tables
app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://test_user:re@localhost/test_db'

class Wikipage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    current_page_id = db.Column(db.Integer, db.ForeignKey('page.id'))
    current_page = db.relationship('Page',
                           backref=db.backref('wiki', lazy='dynamic'))

class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(55))
    text = db.Column(db.Text)
    wikipage_id = db.Column(db.Integer, db.ForeignKey('wikipage.id'))
    wikipage = db.relationship('Wikipage',
                           backref=db.backref('pages', lazy='dynamic'))


db.create_all()