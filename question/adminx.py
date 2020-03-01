import xadmin

from question.models import Choice, Fill, Judge, Program


class ChoiceAdmin(object):
    list_display = ['id', 'question', 'answer_A', 'answer_B', 'answer_C', 'answer_D',
                    'right_answer', 'analysis', 'score', 'level']
    list_filter = ['level']
    search_fields = ['id', 'question']
    list_per_page = 10
    list_editable = ['question']


class FillAdmin(object):
    list_display = ['id', 'question', 'right_answer', 'analysis', 'score', 'level']
    list_filter = ['level']
    search_field = ['id', 'question']
    list_per_page = 10
    list_editable = ['question']


class JudgeAdmin(object):
    list_display = ['id', 'question', 'right_answer', 'analysis', 'score', 'level']
    list_filter = ['level']
    search_field = ['id', 'question']
    list_per_page = 10
    list_editable = ['question']


class ProgramAdmin(object):
    list_display = ['id', 'question', 'answer_template', 'test_case', 'analysis', 'score', 'level']


xadmin.site.register(Choice, ChoiceAdmin)
xadmin.site.register(Fill, FillAdmin)
xadmin.site.register(Judge, JudgeAdmin)
xadmin.site.register(Program, ProgramAdmin)
