import xadmin

from exam.models import Exam
from xadmin.views import CommAdminView, BaseAdminView


# Register your models here.

class GlobalSetting(object):
    # 全局设置
    site_title = '考试管理系统后台'
    site_footer = 'Design by psf'
    # menu_style = 'accordion'


class BaseSetting(object):
    # 启动主题管理器
    enable_themes = True
    # 使用主题
    use_bootswatch = True


class ExamAdmin(object):
    list_display = ['id', 'name', 'exam_date', 'total_time', 'paper', 'institute', 'major', 'tips']
    list_filter = ['institute', 'major', 'exam_date']
    search_fields = ['id', 'name']
    list_per_page = 10
    list_editable = ['name']
    model_icon = 'fa fa-book'


xadmin.site.register(CommAdminView, GlobalSetting)
xadmin.site.register(BaseAdminView, BaseSetting)
xadmin.site.register(Exam, ExamAdmin)
