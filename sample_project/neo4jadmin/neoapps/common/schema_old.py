import datetime
import decimal
import graphene
from graphene_django.types import DjangoObjectType
from graphene.types.generic import GenericScalar
from graphene import ObjectType, String, Schema, relay, Date, DateTime, Time, Decimal, JSONString, Field
from graphene.types.resolver import dict_resolver
import graphql

from django.http import JsonResponse
import json

from neomodel import Traversal


from graphene import ObjectType, String, Schema


class Person(ObjectType):
    full_name = String()

    def resolve_full_name(parent, info):
        return f"{parent.first_name} {parent.last_name}"

def get_human(name):
    return name



class Query(ObjectType):
    # this defines a Field `hello` in our Schema with a single Argument `name`
    hello = String(name=String(default_value="stranger"))
    goodbye = String()

    one_week_from = Date(required=True, date_input=Date(required=True))

    one_hour_from = DateTime(required=True, datetime_input=DateTime(required=True))

    one_hour_from1 = Time(required=True, time_input=Time(required=True))

    add_one_to = Decimal(required=True, decimal_input=Decimal(required=True))

    update_json_key = JSONString(
        required=True,
        json_input=JSONString(required=True),
        key=String(required=True),
        value=String(required=True)
    )

    me = Field(Person)

    def resolve_me(parent, info):
        # returns an object that represents a Person
        return get_human(name="Luke Skywalker")


    """
        query {
            updateJsonKey(jsonInput: "{\"name\": \"Jane\"}", key: "name", value: "Beth")
        }
    """
    def resolve_update_json_key(root, info, json_input, key, value):
        assert json_input == {"name": "Jane"}
        json_input[key] = value
        return json_input

    """
        query {
            addOneTo(decimalInput: "10.50")
        }
    """
    def resolve_add_one_to(root, info, decimal_input):
        assert decimal_input == decimal.Decimal("10.50")
        return decimal_input + decimal.Decimal("1")

    """
        query {
            oneHourFrom(timeInput: "15:04:05")
        }
    """
    def resolve_one_hour_from1(root, info, time_input):
        assert time_input == datetime.time(15, 4, 5)
        tmp_time_input = datetime.datetime.combine(datetime.date(1, 1, 1), time_input)
        return (tmp_time_input + datetime.timedelta(hours=1)).time()

    """
        query {
            oneHourFrom(datetimeInput: "2006-01-02T15:04:05")
        }
    """
    def resolve_one_hour_from(root, info, datetime_input):
        assert datetime_input == datetime.datetime(2006, 1, 2, 15, 4, 5)
        return datetime_input + datetime.timedelta(hours=1)

    """
        query {
            oneWeekFrom(dateInput: "2006-01-02")
        }
    """
    def resolve_one_week_from(root, info, date_input):
        assert date_input == datetime.date(2006, 1, 2)
        return date_input + datetime.timedelta(weeks=1)

    def resolve_hello(root, info, name):
        return f'Hello {name}!'

    def resolve_goodbye(root, info):
        return 'See ya!'

schema = Schema(query=Query)