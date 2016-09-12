from flask_sqlalchemy import SQLAlchemy
from collections import OrderedDict


db = SQLAlchemy()

class asDictable(object):
    def asdict(self):
        result = OrderedDict()
        for key in self.__mapper__.c.keys():
            tmp = getattr(self, key)
            result[key] = tmp
        return result


class Wikipage(db.Model, asDictable):
    id = db.Column(db.Integer, primary_key=True)
    current_page_id = db.Column(db.Integer, db.ForeignKey('page.id'))
    current_page = db.relationship('Page', foreign_keys=current_page_id,
                           backref=db.backref('wiki', lazy='dynamic'))

class Page(db.Model, asDictable):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(55))
    text = db.Column(db.Text)
    wikipage_id = db.Column(db.Integer, db.ForeignKey('wikipage.id'))
    wikipage = db.relationship(Wikipage, foreign_keys=wikipage_id,
                           backref=db.backref('pages', lazy='dynamic'),
                               post_update=True)

