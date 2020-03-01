# Generated by Django 3.0.3 on 2020-03-01 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0002_auto_20200301_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='level',
            field=models.PositiveSmallIntegerField(blank=True, choices=[('1', '入门'), ('2', '简单'), ('3', '普通'), ('4', '较难'), ('5', '困难')], null=True, verbose_name='难度等级'),
        ),
    ]