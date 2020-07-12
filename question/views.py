import subprocess

from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from question.models import Choice, Fill, Judge, Program
from question.serializers import ChoiceSerializer, FillSerializer, JudgeSerializer, ProgramSerializer


# Create your views here.


class ChoiceListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """选择题列表页"""
    # 这里要定义一个默认的排序，否则会报错
    queryset = Choice.objects.all().order_by('id')[:0]
    # 序列化
    serializer_class = ChoiceSerializer

    # 重写queryset
    def get_queryset(self):
        # 题目数量
        choice_number = int(self.request.query_params.get("choice_number"))
        level = int(self.request.query_params.get("level", 1))

        if choice_number:
            self.queryset = Choice.objects.all().filter(level=level).order_by('?')[:choice_number]
        return self.queryset


class FillListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """填空题列表页"""
    # 这里要定义一个默认的排序，否则会报错
    queryset = Fill.objects.all().order_by('id')[:0]
    # 序列化
    serializer_class = FillSerializer

    # 重写queryset
    def get_queryset(self):
        # 题目数量
        fill_number = int(self.request.query_params.get("fill_number"))
        level = int(self.request.query_params.get("level", 1))

        if fill_number:
            self.queryset = Fill.objects.all().filter(level=level).order_by('?')[:fill_number]
        return self.queryset


class JudgeListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """判断题列表页"""
    # 这里要定义一个默认的排序，否则会报错
    queryset = Judge.objects.all().order_by('?')[:0]
    # 序列化
    serializer_class = JudgeSerializer

    # 重写queryset
    def get_queryset(self):
        # 题目数量
        judge_number = int(self.request.query_params.get("judge_number"))
        level = int(self.request.query_params.get("level", 1))

        if judge_number:
            self.queryset = Judge.objects.all().filter(level=level).order_by('?')[:judge_number]
        return self.queryset


class ProgramListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """编程题列表页"""
    # 这里定义一个默认的排序，否则会报错
    queryset = Program.objects.all().order_by('?')[:0]
    # 序列化
    serializer_class = ProgramSerializer

    # 重写queryset
    def get_queryset(self):
        # 题目数量
        program_number = int(self.request.query_params.get("program_number"))
        level = int(self.request.query_params.get("level", 1))

        if program_number:
            self.queryset = Program.objects.all().filter(level=level).order_by('?')[:program_number]
        return self.queryset


class CheckProgramApi(APIView):
    """测试编程题"""

    def post(self, request):
        # 获取post提交的字典数据
        json_body = request.data

        # 将要执行的answer写入python文件
        with open(r'.\question\Solution.py', 'w') as f:
            if json_body['answer']:
                f.write(json_body['answer'])
            else:
                f.write('')
            f.flush()
        # 初始化subprocess
        obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               universal_newlines=True)
        try:
            obj.stdin.write(json_body['program']['test_case'])
            obj.stdin.close()

            cmd_out = obj.stdout.read()
            obj.stdout.close()
            cmd_error = obj.stderr.read()
            obj.stderr.close()
            # print(cmd_out)
            # print(cmd_error)  # 程序没有异常，只输出空行
        except Exception as e:
            return Response({'message': '程序运行出错'})
        finally:
            if 'OK' in cmd_error:
                return Response({'message': 'pass'})
            return Response({'message': cmd_error})
