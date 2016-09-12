from flask_sqlalchemy import SQLAlchemy
from collections import OrderedDict
from sqlalchemy import ForeignKeyConstraint

db = SQLAlchemy()

class asDictable(object):
    def asdict(self):
        result = OrderedDict()
        for key in self.__mapper__.c.keys():
            tmp = getattr(self, key)
            result[key] = tmp
        return result



class Page(db.Model, asDictable):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(55))
    text = db.Column(db.Text)
    wikipage_id = db.Column(db.Integer, db.ForeignKey('wikipage.id'))
    __table_args__ = (
        db.UniqueConstraint("id", "wikipage_id"),
    )
    wikipage = db.relationship('Wikipage',
                            foreign_keys=wikipage_id,
                               )

class Wikipage(db.Model, asDictable):
    id = db.Column(db.Integer, primary_key=True, autoincrement='ignore_fk', )
    current_page_id = db.Column(db.Integer)
    __table_args__ = (
        ForeignKeyConstraint(
            ["id", "current_page_id"],
            ["page.wikipage_id", "page.id"],
            name="fk_current_page"
        ),
    )

    pages = db.relationship(Page, primaryjoin=
                                    id==Page.wikipage_id,
                            foreign_keys=Page.wikipage_id)
    current_page = db.relationship(Page,
                                   primaryjoin=
                                        current_page_id == Page.id,
                                   foreign_keys=current_page_id, post_update=True,
                                   #backref=db.backref('wiki', lazy='dynamic')
                                   )

