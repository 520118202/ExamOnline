# Generated by Django 3.0.3 on 2020-03-01 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('question', '0002_delete_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(blank=True, max_length=200, null=True, verbose_name='题目')),
                ('answer_A', models.CharField(blank=True, max_length=200, null=True, verbose_name='A选项')),
                ('answer_B', models.CharField(blank=True, max_length=200, null=True, verbose_name='B选项')),
                ('answer_C', models.CharField(blank=True, max_length=200, null=True, verbose_name='C选项')),
                ('answer_D', models.CharField(blank=True, max_length=200, null=True, verbose_name='D选项')),
                ('right_answer', models.CharField(blank=True, max_length=1, null=True, verbose_name='正确选项')),
                ('analysis', models.CharField(blank=True, max_length=200, null=True, verbose_name='题目解析')),
                ('score', models.PositiveSmallIntegerField(blank=True, default=2, null=True, verbose_name='分值')),
                ('level', models.PositiveSmallIntegerField(blank=True, choices=[('1', '入门'), ('2', '简单'), ('3', '普通'), ('4', '较难'), ('5', '困难')], null=True, verbose_name='难度等级')),
            ],
            options={
                'verbose_name': '选择题',
                'verbose_name_plural': '选择题',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Fill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(blank=True, max_length=200, null=True, verbose_name='题目')),
                ('right_answer', models.CharField(blank=True, max_length=200, null=True, verbose_name='正确答案')),
                ('analysis', models.CharField(blank=True, max_length=200, null=True, verbose_name='题目解析')),
                ('score', models.PositiveSmallIntegerField(blank=True, default=2, null=True, verbose_name='分值')),
                ('level', models.PositiveSmallIntegerField(blank=True, choices=[('1', '入门'), ('2', '简单'), ('3', '普通'), ('4', '较难'), ('5', '困难')], null=True, verbose_name='难度等级')),
            ],
            options={
                'verbose_name': '填空题',
                'verbose_name_plural': '填空题',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Judge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(blank=True, max_length=200, null=True, verbose_name='题目')),
                ('right_answer', models.CharField(blank=True, max_length=1, null=True, verbose_name='正确答案')),
                ('analysis', models.CharField(blank=True, max_length=200, null=True, verbose_name='题目解析')),
                ('score', models.PositiveSmallIntegerField(blank=True, default=2, null=True, verbose_name='分值')),
                ('level', models.PositiveSmallIntegerField(blank=True, choices=[('1', '入门'), ('2', '简单'), ('3', '普通'), ('4', '较难'), ('5', '困难')], null=True, verbose_name='难度等级')),
            ],
            options={
                'verbose_name': '判断题',
                'verbose_name_plural': '判断题',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(blank=True, max_length=200, null=True, verbose_name='题目')),
                ('right_answer', models.CharField(blank=True, max_length=500, null=True, verbose_name='正确答案')),
                ('test_case', models.CharField(blank=True, max_length=500, null=True, verbose_name='测试用例')),
                ('analysis', models.CharField(blank=True, max_length=200, null=True, verbose_name='题目解析')),
                ('score', models.PositiveSmallIntegerField(blank=True, default=2, null=True, verbose_name='分值')),
                ('level', models.PositiveSmallIntegerField(blank=True, choices=[('1', '入门'), ('2', '简单'), ('3', '普通'), ('4', '较难'), ('5', '困难')], null=True, verbose_name='难度等级')),
            ],
            options={
                'verbose_name': '编程题',
                'verbose_name_plural': '编程题',
                'ordering': ['id'],
            },
        ),
    ]