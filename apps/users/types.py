import graphene_sqlalchemy as gs

from apps.users.models.user import UserModel


class User(gs.SQLAlchemyObjectType):
    class Meta:
        model = UserModel