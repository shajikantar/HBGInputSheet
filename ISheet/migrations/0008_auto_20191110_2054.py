# Generated by Django 2.2.6 on 2019-11-10 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ISheet', '0007_auto_20191109_0006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form_is',
            name='pd_Plat_methodology',
        ),
        migrations.RemoveField(
            model_name='form_is',
            name='pd_methodology',
        ),
    ]
