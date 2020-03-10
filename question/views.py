import subprocess
from django.http import request
from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from question.models import Choice, Fill, Judge, Program
from question.serializers import ChoiceSerializer, FillSerializer, JudgeSerializer, ProgramSerializer


class ChoiceListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """选择题列表页"""
    # 这里要定义一个默认的排序，否则会报错
    queryset = Choice.objects.all().order_by('?')
    # 序列化
    serializer_class = ChoiceSerializer


class FillListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """填空题列表页"""
    # 这里要定义一个默认的排序，否则会报错
    queryset = Fill.objects.all().order_by('?')
    # 序列化
    serializer_class = FillSerializer


class JudgeListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """判断题列表页"""
    # 这里要定义一个默认的排序，否则会报错
    queryset = Judge.objects.all().order_by('?')
    # 序列化
    serializer_class = JudgeSerializer


class ProgramListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """编程题列表页"""
    # 这里定义一个默认的排序，否则会报错
    queryset = Program.objects.all().order_by('?')
    # 序列化
    serializer_class = ProgramSerializer


class CheckProgramApi(APIView):

    def post(self, request):
        # 获取post提交的字典数据
        json_body = request.data
        # 将要执行的answer写入python文件
        with open(r'.\question\Solution.py', 'w') as f:
            f.write(json_body['answer'])
            f.flush()
        # 初始化subprocess
        obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               universal_newlines=True)
        obj.stdin.write(json_body['program']['test_case'])
        obj.stdin.close()

        cmd_out = obj.stdout.read()
        obj.stdout.close()
        cmd_error = obj.stderr.read()
        obj.stderr.close()

        print(cmd_out)
        print(cmd_error)  # 程序没有异常，只输出空行

        if 'OK' in cmd_error:
            print("answer is right")
            return Response({'message': 'OK'})
        return Response({'message': cmd_error})
