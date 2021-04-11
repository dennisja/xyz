from enum import Enum
from datetime import datetime

from sqlalchemy.orm import validates

from core.db import BaseModelMixin, db


class RegistrationMethod(Enum):
    EMAIL = "EMAIL"
    SMS = "SMS"


class UserModel(BaseModelMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.BigInteger, primary_key=True)
    phone = db.Column(db.String(20), unique=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True)
    joined = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    is_verified = db.Column(db.Boolean, nullable=False, default=False)
    registration_method = db.Column(
        db.Enum(RegistrationMethod, name="registration_method_enum"),
        nullable=False,
    )
