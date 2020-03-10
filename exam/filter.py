import django_filters

from exam.models import Exam


class ExamFilter(django_filters.rest_framework.FilterSet):
    """考试过滤的类"""
    # 两个参数，field_name是要过滤的字段，lookup是执行的行为
    exam_date_min = django_filters.DateFilter(field_name='exam_date', lookup_expr='gte')
    exam_date_max = django_filters.DateFilter(field_name="exam_date", lookup_expr='lte')

    class Meta:
        model = Exam
        fields = ['exam_date_min', 'exam_date_max']
