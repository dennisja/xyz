import graphene

from apps.users.models.user import UserModel
from apps.users.types import User
from apps.users.mutations.register import CreateUser


class UserQueries(graphene.ObjectType):
    get_users = graphene.List(User)

    def resolve_get_users(self, info):
        return UserModel.query.all()


class UserMutations(graphene.ObjectType):
    create_user = CreateUser.Field()