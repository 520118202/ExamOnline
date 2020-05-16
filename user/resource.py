from import_export import resources

from user.models import Student


class StudentResource(resources.ModelResource):

    class Meta:
        model = Student
        fields = ('id', 'name', 'user', 'gender', 'clazz')