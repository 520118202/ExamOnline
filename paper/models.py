from django.db import models


# Create your models here.
class Paper(models.Model):
    Level_Type = (
        ('1', '入门'),
        ('2', '简单'),
        ('3', '普通'),
        ('4', '较难'),
        ('5', '困难')
    )
    name = models.CharField("试卷名称", max_length=20, null=True, blank=True)
    score = models.PositiveSmallIntegerField("总分", null=True, blank=True)
    choice_number = models.PositiveSmallIntegerField("选择题数", null=True, blank=True)
    fill_number = models.PositiveSmallIntegerField("填空题数", null=True, blank=True)
    judge_number = models.PositiveSmallIntegerField("判断题数", null=True, blank=True)
    program_number = models.PositiveSmallIntegerField("编程题数", null=True, blank=True)
    level = models.PositiveSmallIntegerField("难度等级", choices=Level_Type, null=True, blank=True)

    class Meta:
        ordering = ["id"]
        db_table = 'paper_info'
        verbose_name = "试卷"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
