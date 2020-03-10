from rest_framework import serializers

from exam.models import Exam, Paper, Grade
from user.serializers import StudentSerializer


class PaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paper
        fields = '__all__'


class ExamSerializer(serializers.ModelSerializer):
    # 覆盖外键字段
    paper = PaperSerializer()

    class Meta:
        model = Exam
        fields = '__all__'


class GradeSerializer(serializers.ModelSerializer):
    # 覆盖外键字段
    exam = ExamSerializer()
    student = StudentSerializer()

    class Meta:
        model = Grade
        fields = '__all__'
