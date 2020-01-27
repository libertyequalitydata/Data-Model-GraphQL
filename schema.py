import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import db_session, Basic as BasicModel, Education as EducationModel, Occupation as OccupationModel, Household as HouseholdModel


class Basic(SQLAlchemyObjectType):
    class Meta:
        model = BasicModel
        interfaces = (relay.Node, )

class BasicConnection(relay.Connection):
    class Meta:
        node = Basic

class Education(SQLAlchemyObjectType):
    class Meta:
        model = EducationModel
        interfaces = (relay.Node, )

class EducationConnection(relay.Connection):
    class Meta:
        node = Education

class Occupation(SQLAlchemyObjectType):
    class Meta:
        model = OccupationModel
        interfaces = (relay.Node, )

class OccupationConnection(relay.Connection):
    class Meta:
        node = Occupation

class Household(SQLAlchemyObjectType):
    class Meta:
        model = HouseholdModel
        interfaces = (relay.Node, )

class HouseholdConnection(relay.Connection):
    class Meta:
        node = Household

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # Allows sorting over multiple columns, by default over the primary key
    all_households = SQLAlchemyConnectionField(Household._meta.connection)
    all_occupations = SQLAlchemyConnectionField(Occupation._meta.connection)
    all_educations = SQLAlchemyConnectionField(Education._meta.connection)
    all_basics = SQLAlchemyConnectionField(Basic._meta.connection, sort=None)

schema = graphene.Schema(query=Query)
