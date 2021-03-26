import graphene
import graphene_sqlalchemy as gs

from apps.users.models.user import UserModel, RegistrationMethod


class User(gs.SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        exclude_fields = ("registration_method",)

    registration_method = graphene.Enum.from_enum(RegistrationMethod)
