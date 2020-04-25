from rest_framework import serializers

from exam.models import Practice
from exam.serializers import PracticeSerializer
from question.models import Choice, Fill, Judge, Program
from question.serializers import ChoiceSerializer, FillSerializer, JudgeSerializer, ProgramSerializer
from record.models import ChoiceRecord, FillRecord, ProgramRecord, JudgeRecord
from user.models import Student
from user.serializers import StudentSerializer


class ChoiceRecordSerializer(serializers.ModelSerializer):
    # 覆盖外键字段 只读
    practice = PracticeSerializer(read_only=True)
    student = StudentSerializer(read_only=True)
    choice = ChoiceSerializer(read_only=True)

    # 用于创建的只写字段
    practice_id = serializers.PrimaryKeyRelatedField(queryset=Practice.objects.all(), source='practice',
                                                     write_only=True)
    student_id = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), source='student', write_only=True)
    choice_id = serializers.PrimaryKeyRelatedField(queryset=Choice.objects.all(), source='choice', write_only=True)

    class Meta:
        model = ChoiceRecord
        fields = '__all__'


class FillRecordSerializer(serializers.ModelSerializer):
    # 覆盖外键字段 只读
    practice = PracticeSerializer(read_only=True)
    student = StudentSerializer(read_only=True)
    fill = FillSerializer(read_only=True)

    # 用于创建的只写字段
    practice_id = serializers.PrimaryKeyRelatedField(queryset=Practice.objects.all(), source='practice',
                                                     write_only=True)
    student_id = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), source='student', write_only=True)
    fill_id = serializers.PrimaryKeyRelatedField(queryset=Fill.objects.all(), source='fill', write_only=True)

    class Meta:
        model = FillRecord
        fields = '__all__'


class JudgeRecordSerializer(serializers.ModelSerializer):
    # 覆盖外键字段 只读
    practice = PracticeSerializer(read_only=True)
    student = StudentSerializer(read_only=True)
    judge = JudgeSerializer(read_only=True)

    # 用于创建的只写字段
    practice_id = serializers.PrimaryKeyRelatedField(queryset=Practice.objects.all(), source='practice',
                                                     write_only=True)
    student_id = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), source='student', write_only=True)
    judge_id = serializers.PrimaryKeyRelatedField(queryset=Judge.objects.all(), source='judge', write_only=True)

    class Meta:
        model = JudgeRecord
        fields = '__all__'


class ProgramRecordSerializer(serializers.ModelSerializer):
    # 覆盖外键字段 只读
    practice = PracticeSerializer(read_only=True)
    student = StudentSerializer(read_only=True)
    program = ProgramSerializer(read_only=True)

    # 用于创建的只写字段
    practice_id = serializers.PrimaryKeyRelatedField(queryset=Practice.objects.all(), source='practice',
                                                     write_only=True)
    student_id = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), source='student', write_only=True)
    program_id = serializers.PrimaryKeyRelatedField(queryset=Program.objects.all(), source='program', write_only=True)

    class Meta:
        model = ProgramRecord
        fields = '__all__'
