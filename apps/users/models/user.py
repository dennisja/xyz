from core.db import BaseModelMixin, db


class UserModel(BaseModelMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(20), unique=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True)
    joined = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
