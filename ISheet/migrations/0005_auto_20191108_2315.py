# Generated by Django 2.2.6 on 2019-11-08 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ISheet', '0004_auto_20191108_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='form_is',
            name='pd_Plat_methodology',
            field=models.CharField(default='NA', max_length=10),
        ),
        migrations.AddField(
            model_name='form_is',
            name='pd_methodology',
            field=models.CharField(default='NA', max_length=4),
        ),
        migrations.AlterField(
            model_name='form_is',
            name='pd_country',
            field=models.CharField(default='NA', max_length=50),
        ),
    ]