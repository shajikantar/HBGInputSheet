# Generated by Django 2.2.6 on 2019-11-08 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ISheet', '0005_auto_20191108_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form_is',
            name='pd_Plat_methodology',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='form_is',
            name='pd_country',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='form_is',
            name='pd_methodology',
            field=models.CharField(default=None, max_length=4),
        ),
    ]
