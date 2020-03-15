from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, mixins, viewsets, filters
from rest_framework.pagination import PageNumberPagination

from exam.filter import ExamFilter
from exam.models import Exam, Grade
from exam.serializers import ExamSerializer, GradeSerializer


# Create your views here.
class CommonPagination(PageNumberPagination):
    """考试列表自定义分页"""
    # 默认每页显示的个数
    page_size = 2
    # 可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    # 页码参数
    page_query_param = 'page'
    # 最多能显示多少页
    max_page_size = 100


class ExamListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """考试列表页"""
    # 这里必须要定义一个默认的排序,否则会报错
    queryset = Exam.objects.all().order_by('id')
    # 序列化
    serializer_class = ExamSerializer
    # 分页
    pagination_class = CommonPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # 设置filter的类为我们自定义的类
    filter_class = ExamFilter
    # 搜索,=name表示精确搜索，也可以使用各种正则表达式
    search_fields = ('name', 'major')
    # 排序
    ordering_fields = ('id', 'exam_date')


class GradeListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """成绩列表"""
    # 这里必须要定义一个默认的排序,否则会报错
    queryset = Grade.objects.all().order_by('-create_time')
    # 序列化
    serializer_class = GradeSerializer
    # 分页
    pagination_class = CommonPagination