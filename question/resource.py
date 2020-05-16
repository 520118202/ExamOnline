from import_export import resources

from question.models import Choice, Fill, Judge, Program


class ChoiceResource(resources.ModelResource):
    class Meta:
        model = Choice
        fields = ('question', 'answer_A', 'answer_B', 'answer_C', 'answer_D', 'right_answer', 'analysis', 'score', 'level')


class FillResource(resources.ModelResource):
    class Meta:
        model = Fill
        fields = ('question', 'right_answer', 'analysis', 'score', 'level')


class JudgeResource(resources.ModelResource):
    class Meta:
        model = Judge
        fields = ('question', 'right_answer', 'analysis', 'score', 'level')


class ProgramResource(resources.ModelResource):
    class Meta:
        model = Program
        fields = ('question', 'answer_template', 'test_case', 'analysis', 'score', 'level')