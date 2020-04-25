from django.db import models


# Create your models here.
class Choice(models.Model):
    """选择题模型"""
    LEVEL_CHOICES = (
        ('1', '入门'),
        ('2', '简单'),
        ('3', '普通'),
        ('4', '较难'),
        ('5', '困难')
    )
    ANSWER_CHOICES = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D')
    )
    question = models.TextField("题目", default="")
    answer_A = models.CharField("A选项", max_length=200, default="")
    answer_B = models.CharField("B选项", max_length=200, default="")
    answer_C = models.CharField("C选项", max_length=200, default="")
    answer_D = models.CharField("D选项", max_length=200, default="")
    right_answer = models.CharField("正确选项", max_length=1, choices=ANSWER_CHOICES, default="A")
    analysis = models.TextField("题目解析", default="暂无")
    score = models.PositiveSmallIntegerField("分值", default=2)
    level = models.CharField("难度等级", max_length=1, choices=LEVEL_CHOICES, default='1')

    class Meta:
        ordering = ['id']
        verbose_name = '选择题'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.question


class Fill(models.Model):
    """判断题模型"""
    LEVEL_CHOICES = (
        ('1', '入门'),
        ('2', '简单'),
        ('3', '普通'),
        ('4', '较难'),
        ('5', '困难')
    )
    question = models.TextField("题目", default="")
    right_answer = models.CharField("正确答案", max_length=200, default="")
    analysis = models.TextField("题目解析", default="暂无")
    score = models.PositiveSmallIntegerField("分值", default=2)
    level = models.CharField("难度等级", max_length=1, choices=LEVEL_CHOICES, default='1')

    class Meta:
        ordering = ['id']
        verbose_name = '填空题'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.question


class Judge(models.Model):
    """判断题模型"""
    LEVEL_CHOICES = (
        ('1', '入门'),
        ('2', '简单'),
        ('3', '普通'),
        ('4', '较难'),
        ('5', '困难')
    )
    ANSWER_CHOICES = (
        ('T', '正确'),
        ('F', '错误')
    )
    question = models.TextField("题目", default="")
    right_answer = models.CharField("正确答案", max_length=1, choices=ANSWER_CHOICES, default="T")
    analysis = models.TextField("题目解析", default="暂无")
    score = models.PositiveSmallIntegerField("分值", default=2)
    level = models.CharField("难度等级", max_length=1, choices=LEVEL_CHOICES, default='1')

    class Meta:
        ordering = ['id']
        verbose_name = '判断题'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.question


class Program(models.Model):
    """编程题模型"""
    LEVEL_CHOICES = (
        ('1', '入门'),
        ('2', '简单'),
        ('3', '普通'),
        ('4', '较难'),
        ('5', '困难')
    )
    question = models.TextField("题目", max_length=200, default="")
    answer_template = models.TextField("答题模板", default="")
    test_case = models.TextField("测试用例", default="")
    analysis = models.TextField("题目解析", default="")
    score = models.PositiveSmallIntegerField("分值", default=8)
    level = models.CharField("难度等级", max_length=1, choices=LEVEL_CHOICES, default='1')

    class Meta:
        ordering = ['id']
        verbose_name = '编程题'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.question