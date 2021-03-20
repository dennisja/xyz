from graphene import ObjectType, Schema
from apps.users.schema import UserQueries


class Query(UserQueries, ObjectType):
    pass


schema = Schema(query=Query)