from django.contrib.sites.shortcuts import get_current_site
from django.contrib.sites.models import Site
import datetime
import graphene
from graphene_django.types import DjangoObjectType
from graphene.types.generic import GenericScalar
from graphene import ObjectType, String, Schema, relay
from neoapps.common.models import Language, Country, Category
from neoapps.common.defs import CategoryType, CountryType, LanguageType
from graphene.types.resolver import dict_resolver
import graphql
import graphene_django_optimizer as gql_optimizer
from django.http import JsonResponse
import json

from neomodel import Traversal

from neomodel_admin import utils


class Query(ObjectType):
    categories = graphene.List(CategoryType)
    category = graphene.Field(CategoryType, id=graphene.Int())

    languages = graphene.List(LanguageType)
    language = graphene.Field(LanguageType, id=graphene.Int())
    
    countries = graphene.List(CountryType)
    country = graphene.Field(CountryType, id=graphene.Int())

    def resolve_categories(self, info, **kwargs):
        categories = Category.nodes.all()
        return categories

    def resolve_category(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            category = utils.get_by_id(Category, id)
            return category

    def resolve_countries(self, info, **kwargs):
        countries = Country.nodes.all()
        return countries

    def resolve_country(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            country = utils.get_by_id(Country, id)
            return country

    def resolve_languages(self, info, **kwargs):
        languages = Language.nodes.all()
        return languages

    def resolve_language(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            language = utils.get_by_id(Language, id)
            return language


schema = Schema(query=Query)
