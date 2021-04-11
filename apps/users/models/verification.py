from core.db import db, BaseModelMixin
from datetime import datetime


class VerificationCodeModel(BaseModelMixin, db.Model):
    __tablename__ = "verification_codes"

    id = db.Column(db.BigInteger, primary_key=True)
    is_used = db.Column(db.Boolean, nullable=False, default=False)
    code = db.Column(db.String(6), nullable=False)
    user_id = db.Column(db.BigInteger, db.ForeignKey("users.id"), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
