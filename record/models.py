from django.db import models

# Create your models here.
from exam.models import Practice
from question.models import Choice, Fill, Judge, Program
from user.models import Student


class Record(models.Model):
    """练习记录"""
    practice = models.ForeignKey(Practice, verbose_name="练习", on_delete=models.CASCADE)
    student = models.ForeignKey(Student, verbose_name="学生", on_delete=models.CASCADE)
    your_answer = models.TextField("你的作答", null=True, blank=True)

    class Meta:
        # 抽象类
        abstract = True

    def __str__(self):
        return self.your_answer


class ChoiceRecord(Record):
    """选择题答题记录"""
    choice = models.ForeignKey(Choice, verbose_name="选择题", on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']
        verbose_name = '选择题答题记录'
        verbose_name_plural = verbose_name


class FillRecord(Record):
    """填空题答题记录"""
    fill = models.ForeignKey(Fill, verbose_name="填空题", on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']
        verbose_name = '填空题答题记录'
        verbose_name_plural = verbose_name


class JudgeRecord(Record):
    judge = models.ForeignKey(Judge, verbose_name="判断题", on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']
        verbose_name = '判断题答题记录'
        verbose_name_plural = verbose_name


class ProgramRecord(Record):
    program = models.ForeignKey(Program, verbose_name="编程题", on_delete=models.CASCADE)
    cmd_msg = models.TextField("输出结果", null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = '编程题答题记录'
        verbose_name_plural = verbose_name
