import graphene

class CategoryType(graphene.ObjectType):
    id = graphene.ID()
    uid = graphene.ID()
    title = graphene.String()


class CategoryInput(graphene.InputObjectType):
    title = graphene.String()


class CountryType(graphene.ObjectType):
    id = graphene.ID()
    uid = graphene.ID()
    country_name = graphene.String()
    country_code = graphene.String()
    iso_code = graphene.String()
    is_active = graphene.String()


class LanguageType(graphene.ObjectType):
    id = graphene.ID()
    uid = graphene.ID()
    name = graphene.String()
    iso = graphene.String()
    is_active = graphene.String()