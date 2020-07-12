from django.contrib.auth.models import AbstractUser, User
from django.db import models


# Create your models here.
class Clazz(models.Model):
    """班级"""
    year = models.CharField("年级", max_length=20)
    major = models.CharField("专业", max_length=20)
    clazz = models.CharField("班级", max_length=20)

    class Meta:
        ordering = ['id']
        verbose_name = "班级"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.year + self.major + self.clazz


class Student(models.Model):
    """学生模型类"""
    GENDER_CHOICES = (
        ('m', '男'),
        ('f', '女')
    )
    name = models.CharField("姓名", max_length=20, default="")
    # 一对一关联字段
    user = models.OneToOneField(User, verbose_name="用户", on_delete=models.CASCADE)
    gender = models.CharField("性别", max_length=1, choices=GENDER_CHOICES, default="")
    clazz = models.ForeignKey(Clazz, verbose_name="班级", on_delete=models.CASCADE, default="1")


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
