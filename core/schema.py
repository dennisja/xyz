from graphene import ObjectType, Schema
from apps.users.schema import UserQueries, UserMutations


class Query(UserQueries, ObjectType):
    pass


class Mutation(UserMutations, ObjectType):
    pass


schema = Schema(query=Query, mutation=Mutation)
