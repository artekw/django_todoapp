# Generated by Django 2.1.7 on 2019-02-23 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0011_auto_20190223_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Termin zadania'),
        ),
    ]