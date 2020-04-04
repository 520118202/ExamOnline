from django.contrib.auth.models import AbstractUser, User
from django.db import models


# Create your models here.
class Student(models.Model):
    """学生模型类"""
    GENDER_CHOICES = (
        ('m', '男'),
        ('f', '女')
    )
    GRADE_CHOICES = (
        ('2016', '2016级'),
        ('2017', '2017级'),
        ('2018', '2018级'),
        ('2019', '2019级')
    )
    name = models.CharField("姓名", max_length=20, default="")
    gender = models.CharField("性别", max_length=1, choices=GENDER_CHOICES, default="")
    year = models.CharField("年级", max_length=4, choices=GRADE_CHOICES, default="")
    major = models.CharField("专业", max_length=20, default="")
    clazz = models.CharField("班级", max_length=20, default="")

    # 一对一关联字段
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="用户")

    class Meta:
        ordering = ['id']
        db_table = 'user_student'
        verbose_name = '学生'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Teacher(models.Model):
    "教师模型类"
    GENDER_CHOICES = (
        ('男', '男'),
        ('女', '女')
    )
    TITLE_CHOICES = (
        ('讲师', '讲师'),
        ('副教授', '副教授'),
        ('教授', '教授')
    )
    name = models.CharField("姓名", max_length=20, default="")
    gender = models.CharField("性别", max_length=1, choices=GENDER_CHOICES, default="男")
    title = models.CharField("职称", max_length=5, choices=TITLE_CHOICES, default="讲师")
    institute = models.CharField("学院", max_length=20, default="")

    # 一对一关联字段
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="用户")

    class Meta:
        ordering = ['id']
        db_table = 'user_teacher'
        verbose_name = '教师'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
