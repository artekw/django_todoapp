# Generated by Django 2.1.5 on 2019-02-02 10:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='created_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
