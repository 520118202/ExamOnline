import xadmin

from user.models import Student, Teacher


class StudentAdmin(object):
    list_display = ['id', 'name', 'user', 'gender', 'year', 'major', 'clazz']
    list_filter = ['gender', 'year', 'major', 'clazz']
    search_fields = ['id', 'name']
    list_display_links = ['name']
    list_per_page = 10
    model_icon = 'fa fa-user-circle-o'
    relfield_style = 'fk-ajax'


class TeacherAdmin(object):
    list_display = ['id', 'name', 'user', 'gender', 'title', 'institute']
    list_filter = ['gender', 'title', 'institute']
    search_fields = ['id', 'name']
    list_display_links = ['name']
    list_per_page = 10
    model_icon = 'fa fa-graduation-cap'


xadmin.site.register(Student, StudentAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
