# Generated by Django 3.0.3 on 2020-03-01 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0003_choice_fill_judge_program'),
    ]

    operations = [
        migrations.RenameField(
            model_name='program',
            old_name='right_answer',
            new_name='answer_template',
        ),
        migrations.AlterField(
            model_name='choice',
            name='level',
            field=models.PositiveSmallIntegerField(blank=True, choices=[('1', '入门'), ('2', '简单'), ('3', '普通'), ('4', '较难'), ('5', '困难')], default=1, null=True, verbose_name='难度等级'),
        ),
        migrations.AlterField(
            model_name='fill',
            name='level',
            field=models.PositiveSmallIntegerField(blank=True, choices=[('1', '入门'), ('2', '简单'), ('3', '普通'), ('4', '较难'), ('5', '困难')], default=1, null=True, verbose_name='难度等级'),
        ),
        migrations.AlterField(
            model_name='judge',
            name='level',
            field=models.PositiveSmallIntegerField(blank=True, choices=[('1', '入门'), ('2', '简单'), ('3', '普通'), ('4', '较难'), ('5', '困难')], default=1, null=True, verbose_name='难度等级'),
        ),
        migrations.AlterField(
            model_name='program',
            name='analysis',
            field=models.TextField(blank=True, null=True, verbose_name='题目解析'),
        ),
        migrations.AlterField(
            model_name='program',
            name='level',
            field=models.PositiveSmallIntegerField(blank=True, choices=[('1', '入门'), ('2', '简单'), ('3', '普通'), ('4', '较难'), ('5', '困难')], default=1, null=True, verbose_name='难度等级'),
        ),
        migrations.AlterField(
            model_name='program',
            name='score',
            field=models.PositiveSmallIntegerField(blank=True, default=8, null=True, verbose_name='分值'),
        ),
        migrations.AlterField(
            model_name='program',
            name='test_case',
            field=models.TextField(blank=True, null=True, verbose_name='测试用例'),
        ),
    ]