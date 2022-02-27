from uuid import uuid4

from graphene_pynamodb.relationships import OneToOne
from pynamodb.attributes import UnicodeAttribute
from pynamodb.models import Model


class Department(Model):
    class Meta:
        table_name = "my_department"
        region = 'cn-northwest-1'

    id = UnicodeAttribute(hash_key=True)
    name = UnicodeAttribute(null=False)


# if not Department.exists():
#     Department.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
#     dev = Department(id='001', name="开发")
#     dev.save()
#     test = Department(id='002', name="测试")
#     test.save()
# else:
#     Department.delete_table()


class User(Model):
    class Meta:
        table_name = "my_users"
        region = 'cn-northwest-1'

    id = UnicodeAttribute(hash_key=True)
    name = UnicodeAttribute(null=False)
    department = OneToOne(Department)


# if not User.exists():
#     User.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
#     User(id=str(uuid4()), name="John Snow", department=dev).save()
#     User(id=str(uuid4()), name="Daenerys Targaryen", department=test).save()
# else:
#     User.delete_table()
