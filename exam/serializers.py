from rest_framework import serializers

from exam.models import Exam, Paper, Grade, Practice
from user.models import Student
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
    # 覆盖外键字段 只读
    exam = ExamSerializer(read_only=True)
    student = StudentSerializer(read_only=True)

    # 用于创建的只写字段
    exam_id = serializers.PrimaryKeyRelatedField(queryset=Exam.objects.all(), source='exam', write_only=True)
    student_id = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), source='student', write_only=True)

    class Meta:
        model = Grade
        fields = '__all__'


class PracticeSerializer(serializers.ModelSerializer):
    # 覆盖外键字段 只读
    student = StudentSerializer(read_only=True)

    # 用于创建的只写字段
    student_id = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), source='student', write_only=True)

    class Meta:
        model = Practice
        fields = '__all__'
