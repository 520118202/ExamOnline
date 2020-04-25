import xadmin
from django.contrib.auth.models import User
from xadmin.plugins.auth import UserAdmin

from exam.models import Exam, Grade, Paper
from xadmin.views import CommAdminView, BaseAdminView


# Register your models here.

class GlobalSetting(object):
    # 全局设置
    site_title = 'Python在线考试后台管理系统'
    site_footer = 'Design by Pengshengfu'
    # 菜单默认收缩
    # menu_style = 'accordion'


class BaseSetting(object):
    # 启动主题管理器
    enable_themes = True
    # 使用主题
    use_bootswatch = True


class ExamAdmin(object):
    list_display = ['id', 'name', 'exam_date', 'total_time', 'paper', 'major', 'tips', 'clazzs']
    list_filter = ['major', 'exam_date']
    search_fields = ['id', 'name']
    list_display_links = ['name']
    list_per_page = 10
    # list_editable = ['name']
    model_icon = 'fa fa-book'
    relfield_style = 'fk-ajax'
    # 多对多样式字段支持过滤
    filter_horizontal = ('clazzs',)
    # 修改多对多穿梭框样式
    style_fields = {'clazzs': 'm2m_transfer'}


class PaperAdmin(object):
    list_display = ['id', 'name', 'score', 'choice_number', 'fill_number', 'judge_number', 'program_number', 'level']
    list_filter = ['level']
    search_fields = ['id', 'name']
    list_display_links = ['name']
    list_per_page = 10
    # list_editable = ['name']
    model_icon = 'fa fa-file-text'


class GradeAdmin(object):
    list_display = ['id', 'exam', 'student', 'score', 'create_time', 'update_time']
    list_filter = ['exam', 'student', 'create_time', 'update_time']
    search_fields = ['exam', 'student']
    list_display_links = ['score']
    list_per_page = 10
    # list_editable = ['id', 'score']
    model_icon = 'fa fa-bar-chart'

    data_charts = {
        'grade_charts1': {
            'title': '考试成绩曲线图',
            'x-field': 'create_time',
            'y-field': ('score',),
            'order': ('id',)
        },
        'grade_charts2': {
            'title': '考试成绩柱状图',
            'x-field': 'score',
            'y-field': ('score',),
            'order': ('id',),
            'option': {
                "series": {"bars": {"align": "center", "barWidth": 0.5, "show": True}},
                "xaxis": {"aggregate": "count", "mode": "score"}
            }
        }
    }


xadmin.site.register(CommAdminView, GlobalSetting)
xadmin.site.register(BaseAdminView, BaseSetting)
xadmin.site.register(Exam, ExamAdmin)
xadmin.site.register(Paper, PaperAdmin)
xadmin.site.register(Grade, GradeAdmin)
