from import_export import resources, fields

from user.models import Student


class StudentResource(resources.ModelResource):

    class Meta:
        model = Student
        fields = ('id', 'name', 'user', 'gender', 'clazz')
        # id = fields.Field(attribute='id', column_name='ID')
        # name = fields.Field(attribute='name', column_name='姓名')
        # user = fields.Field(attribute='user', column_name='用户')
        # gender = fields.Field(attribute='gender', column_name='性别')
        # clazz = fields.Field(attribute='clazz', column_name='班级')