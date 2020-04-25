from django.db import models
from question.models import Choice, Fill, Judge, Program
from user.models import Student, Clazz
from datetime import datetime
import random


# Create your models here.
class Paper(models.Model):
    """试卷模型类"""
    LEVEL_CHOICES = (
        ('1', '入门'),
        ('2', '简单'),
        ('3', '普通'),
        ('4', '较难'),
        ('5', '困难')
    )
    name = models.CharField("试卷名称", max_length=20, default="")
    score = models.PositiveSmallIntegerField("总分", default=100)
    choice_number = models.PositiveSmallIntegerField("选择题数", default=10)
    fill_number = models.PositiveSmallIntegerField("填空题数", default=10)
    judge_number = models.PositiveSmallIntegerField("判断题数", default=10)
    program_number = models.PositiveSmallIntegerField("编程题数", default=5)
    level = models.CharField("难度等级", max_length=1, choices=LEVEL_CHOICES, default="1")

    class Meta:
        ordering = ["id"]
        verbose_name = "试卷"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.score = (self.choice_number + self.fill_number + self.judge_number) * 2 + self.program_number * 8
        super().save(*args, **kwargs)


class Exam(models.Model):
    """考试模型类"""
    name = models.CharField("考试名称", max_length=20, default="")
    exam_date = models.DateField("考试日期", default="")
    total_time = models.PositiveSmallIntegerField("时长", default=120, help_text="时长按照分钟填写")
    paper = models.OneToOneField(Paper, on_delete=models.CASCADE, verbose_name="试卷", default="")
    major = models.CharField("专业", max_length=20, default="")
    tips = models.TextField("考生须知", default="")
    clazzs = models.ManyToManyField(Clazz, verbose_name="参加考试的班级")

    class Meta:
        ordering = ["id"]
        db_table = 'exam_info'
        verbose_name = "考试"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Grade(models.Model):
    """成绩模型类"""
    exam = models.ForeignKey(Exam, verbose_name="考试", on_delete=models.CASCADE)
    student = models.ForeignKey(Student, verbose_name="学生", on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField("分数", default="")
    create_time = models.DateTimeField("创建日期", auto_now_add=True)
    update_time = models.DateTimeField("修改日期", auto_now=True)

    class Meta:
        ordering = ['id']
        verbose_name = '成绩'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.id}的{self.student}为{self.score}分'


class Practice(models.Model):
    """模拟练习"""
    name = models.CharField("练习名称", max_length=20)
    student = models.ForeignKey(Student, verbose_name="学生", on_delete=models.CASCADE)
    create_time = models.DateTimeField("练习时间", auto_now_add=True)

    class Meta:
        ordering = ['id']
        verbose_name = '练习'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = f'模拟练习{datetime.now().strftime("%Y%m%d")}{random.randint(1000, 9999)}'
        super().save(*args, **kwargs)
