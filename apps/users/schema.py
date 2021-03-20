import graphene

from apps.users.models.user import UserModel
from apps.users.types import User


class UserQueries(graphene.ObjectType):
    get_users = graphene.List(User)

    def resolve_get_users(self, info):
        return UserModel.query.all()