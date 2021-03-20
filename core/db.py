from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BaseModelMixin(object):
    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()