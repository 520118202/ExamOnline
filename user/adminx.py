import xadmin

from user.models import Student, Teacher, Clazz


class ClazzAdmin(object):
    list_display = ['id', 'year', 'major', 'clazz']
    list_filter = ['year', 'major']
    search_fields = ['id', 'year', 'major', 'clazz']
    list_display_links = ['clazz']
    list_per_page = 10
    # list_editable = ['name']
    model_icon = 'fa fa-file-text'


class StudentAdmin(object):
    list_display = ['id', 'name', 'user', 'gender', 'clazz']
    list_filter = ['gender', 'clazz']
    search_fields = ['id', 'name', 'clazz']
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
xadmin.site.register(Clazz, ClazzAdmin)
