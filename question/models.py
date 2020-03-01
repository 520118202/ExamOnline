from django.db import models


# Create your models here.
class Choice(models.Model):
    Level_Type = (
        ('1', '入门'),
        ('2', '简单'),
        ('3', '普通'),
        ('4', '较难'),
        ('5', '困难')
    )
    question = models.CharField("题目", max_length=200, null=True, blank=True)
    answer_A = models.CharField("A选项", max_length=200, null=True, blank=True)
    answer_B = models.CharField("B选项", max_length=200, null=True, blank=True)
    answer_C = models.CharField("C选项", max_length=200, null=True, blank=True)
    answer_D = models.CharField("D选项", max_length=200, null=True, blank=True)
    right_answer = models.CharField("正确选项", max_length=1, null=True, blank=True)
    analysis = models.CharField("题目解析", max_length=200, null=True, blank=True)
    score = models.PositiveSmallIntegerField("分值", default=2, null=True, blank=True)
    level = models.PositiveSmallIntegerField("难度等级", choices=Level_Type, default=1, null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = '选择题'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.question


class Fill(models.Model):
    Level_Type = (
        ('1', '入门'),
        ('2', '简单'),
        ('3', '普通'),
        ('4', '较难'),
        ('5', '困难')
    )
    question = models.CharField("题目", max_length=200, null=True, blank=True)
    right_answer = models.CharField("正确答案", max_length=200, null=True, blank=True)
    analysis = models.CharField("题目解析", max_length=200, null=True, blank=True)
    score = models.PositiveSmallIntegerField("分值", default=2, null=True, blank=True)
    level = models.PositiveSmallIntegerField("难度等级", choices=Level_Type, default=1, null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = '填空题'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.question


class Judge(models.Model):
    Level_Type = (
        ('1', '入门'),
        ('2', '简单'),
        ('3', '普通'),
        ('4', '较难'),
        ('5', '困难')
    )
    question = models.CharField("题目", max_length=200, null=True, blank=True)
    right_answer = models.CharField("正确答案", max_length=1, null=True, blank=True)
    analysis = models.CharField("题目解析", max_length=200, null=True, blank=True)
    score = models.PositiveSmallIntegerField("分值", default=2, null=True, blank=True)
    level = models.PositiveSmallIntegerField("难度等级", choices=Level_Type, default=1, null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = '判断题'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.question


class Program(models.Model):
    Level_Type = (
        ('1', '入门'),
        ('2', '简单'),
        ('3', '普通'),
        ('4', '较难'),
        ('5', '困难')
    )
    question = models.CharField("题目", max_length=200, null=True, blank=True)
    answer_template = models.CharField("正确答案", max_length=500, null=True, blank=True)
    test_case = models.TextField("测试用例", null=True, blank=True)
    analysis = models.TextField("题目解析", null=True, blank=True)
    score = models.PositiveSmallIntegerField("分值", default=8, null=True, blank=True)
    level = models.PositiveSmallIntegerField("难度等级", choices=Level_Type, default=1, null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = '编程题'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.question
