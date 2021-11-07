
from neomodel import StructuredNode, BooleanProperty, StructuredRel, UniqueIdProperty, StringProperty, DateTimeProperty, Relationship, RelationshipFrom, RelationshipTo, One, OneOrMore
from django_neomodel import DjangoNode
from django.utils.translation import ugettext_lazy as _


class Category(DjangoNode):
    uid = UniqueIdProperty()
    title = StringProperty(unique_index=True)

    related = Relationship('Category', 'RELATED')


    class Meta:
        app_label = _('Library')

    def __str__(self):
        return self.title

class Country(DjangoNode):
    uid = UniqueIdProperty()
    country_code = StringProperty(max_length=10, unique_index=True)
    iso_code = StringProperty(max_length=10, unique_index=True)
    country_name = StringProperty(max_length=150)
    is_active = BooleanProperty()

    author = RelationshipFrom('neoapps.user.models.User', 'LIVES_IN', cardinality=One)

    class Meta:
        verbose_name = _("Neo Country")
        verbose_name_plural = _("Neo Country")
        app_label = _('Library')

    def __str__(self):
        return self.country_name
        

class Language(DjangoNode):
    uid = UniqueIdProperty()
    name = StringProperty(max_length=50)
    iso = StringProperty(max_length=10, unique_index=True)
    is_active = BooleanProperty()

    author = RelationshipFrom('neoapps.user.models.User', 'CAN_SPEAK', cardinality=OneOrMore)

    class Meta:
        verbose_name = _("Neo Language")
        verbose_name_plural = _("Neo Language")
        app_label = _('Library')

    def __str__(self):
        return self.name


class Review(DjangoNode):
    uid = UniqueIdProperty()
    text = StringProperty()
    created_at = DateTimeProperty()

    class Meta:
        verbose_name = _("Review")
        verbose_name_plural = _("Reviews")

    def __str__(self):
        return str(self.uid)