import xadmin

from question.models import Choice, Fill, Judge, Program


class ChoiceAdmin(object):
    list_display = ['id', 'question', 'answer_A', 'answer_B', 'answer_C', 'answer_D',
                    'right_answer', 'analysis', 'score', 'level']
    list_filter = ['level']
    search_fields = ['id', 'question']
    list_display_links = ['question']
    list_per_page = 10
    list_editable = ['question']
    model_icon = 'fa fa-question-circle-o'


class FillAdmin(object):
    list_display = ['id', 'question', 'right_answer', 'analysis', 'score', 'level']
    list_filter = ['level']
    search_field = ['id', 'question']
    list_display_links = ['question']
    list_per_page = 10
    list_editable = ['question']
    model_icon = 'fa fa-edit '


class JudgeAdmin(object):
    list_display = ['id', 'question', 'right_answer', 'analysis', 'score', 'level']
    list_filter = ['level']
    search_field = ['id', 'question']
    list_display_links = ['question']
    list_per_page = 10
    list_editable = ['question']
    model_icon = 'fa fa-check-square-o'


class ProgramAdmin(object):
    list_display = ['id', 'question', 'answer_template', 'test_case', 'analysis', 'score', 'level']
    list_filter = ['level']
    search_field = ['id', 'question']
    list_display_links = ['question']
    list_per_page = 10
    list_editable = ['question']
    model_icon = 'fa fa-laptop'


xadmin.site.register(Choice, ChoiceAdmin)
xadmin.site.register(Fill, FillAdmin)
xadmin.site.register(Judge, JudgeAdmin)
xadmin.site.register(Program, ProgramAdmin)
