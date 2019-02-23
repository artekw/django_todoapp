# Generated by Django 2.1.7 on 2019-02-23 09:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0008_auto_20190223_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='todoapp.TaskCategory', verbose_name='Kategoria'),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Data dodania zadania'),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, max_length=200, verbose_name='Opis zadania'),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data wykonania zadania'),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_done',
            field=models.BooleanField(default=False, verbose_name='Data zakończenia zadania'),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_important',
            field=models.BooleanField(default=False, verbose_name='Pilne!'),
        ),
    ]