import re

import graphene
import schema
from graphql import GraphQLError
from email_validator import validate_email
from sqlalchemy import or_

from apps.users.models.user import UserModel, RegistrationMethod
from apps.users.types import User

NON_WORD_CHARACTERS_REGEX = re.compile(r"\W+")

no_non_word_characters = lambda word: not NON_WORD_CHARACTERS_REGEX.search(word)


def get_valid_email(email: str):
    try:
        return validate_email(
            email, check_deliverability=False, allow_smtputf8=False
        ).email
    except exc:
        raise "Invalid Email"


create_user_validation_schema = schema.Schema(
    {
        schema.Optional("email"): schema.And(
            str,
            schema.Use(
                str.strip,
            ),
            schema.Use(get_valid_email, error="Invalid email"),
        ),
        schema.Optional("phone"): schema.And(
            str,
            schema.Use(
                str.strip,
            ),
            lambda phone: 1 < len(phone) < 25,
            error="The phone number used is invalid",
        ),
        "registration_method": schema.And(
            lambda method: method in [method.value for method in RegistrationMethod],
            error="Invalid registration method",
        ),
        "username": schema.And(
            str,
            schema.Use(str.lower),
            no_non_word_characters,
            error="Invalid username",
        ),
    }
)


class CreateUserInput(graphene.InputObjectType):
    email = graphene.String(description="The email of the user")
    phone = graphene.String(description="The phone number of the user")
    username = graphene.String(required=True, description="The username of the user")
    registration_method = graphene.Field(
        graphene.Enum.from_enum(
            RegistrationMethod,
        ),
        description="The method used when registering",
        required=True,
    )


class CreateUser(graphene.Mutation):
    class Arguments:
        create_user_input = CreateUserInput(required=True)

    create_success = graphene.Boolean()
    user = graphene.Field(User)

    def mutate(root, info, create_user_input=None):
        valid_user_input = create_user_validation_schema.validate(create_user_input)
        email = valid_user_input.get("email")
        username = valid_user_input.get("username")
        phone = valid_user_input.get("phone")
        registration_method = valid_user_input.get("registration_method")

        # TODO: use the validation schema for this (or implement them as strategies)
        if not email and RegistrationMethod.EMAIL.value == registration_method:
            raise GraphQLError("Cannot register user by email without an email")

        if not phone and RegistrationMethod.SMS.value == registration_method:
            raise GraphQLError("Cannot register user by phone without a phone number")

        filter_conditions = [
            (UserModel.username == username),
        ]
        if email:
            filter_conditions.append((UserModel.email == email))
        if phone:
            filter_conditions.append((UserModel.phone == phone))

        user_exists = UserModel.query.filter(or_(*filter_conditions)).first()

        if user_exists:
            raise GraphQLError(
                # TODO: maybe handle each case separately i.e for phone, email and phone number
                "Either username, email or phone entered is already in use"
            )

        user = UserModel(
            email=email,
            username=username,
            phone=phone,
            registration_method=RegistrationMethod.EMAIL,
        )
        user.save()

        # TODO: implement verification here
        # generate verification code for the user
        # send them an email if they registered by email
        # TODO: send them an SMS if they registered by phone
        # TODO: if they registered by a social auth provider just do nothing
        return CreateUser(create_success=True, user=user)
