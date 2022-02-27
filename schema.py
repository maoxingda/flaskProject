import graphene
from graphene_pynamodb import PynamoObjectType

from models import User, Department


class UserNode(PynamoObjectType):
    class Meta:
        model = User
        interfaces = (graphene.Node,)


class DeptNode(PynamoObjectType):
    class Meta:
        model = Department
        interfaces = (graphene.Node,)


class Query(graphene.ObjectType):
    users = graphene.List(UserNode)
    depts = graphene.List(DeptNode)

    @staticmethod
    def resolve_users(root, info):
        return list(User.scan())

    @staticmethod
    def resolve_depts(root, info):
        return list(Department.scan())


schema = graphene.Schema(query=Query)
