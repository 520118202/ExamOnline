from django.db import models
from paper.models import Paper


# Create your models here.
class Exam(models.Model):
    name = models.CharField("考试名称", max_length=20)
    exam_date = models.DateField("考试日期", null=True, blank=True)
    total_time = models.TimeField("时长", null=True, blank=True, help_text="时长按照分钟填写")
    paper = models.OneToOneField(Paper, on_delete=models.CASCADE, verbose_name="试卷", null=True, blank=True)
    institute = models.CharField("学院", max_length=20, null=True, blank=True)
    major = models.CharField("专业", max_length=20, null=True, blank=True)
    tips = models.TextField("考生须知", null=True, blank=True)

    class Meta:
        ordering = ["id"]
        db_table = 'exam_info'
        verbose_name = "考试"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
