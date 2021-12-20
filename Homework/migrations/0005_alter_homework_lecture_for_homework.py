# Generated by Django 3.2.6 on 2021-12-19 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Lecture', '0003_alter_lecture_course'),
        ('Homework', '0004_alter_homework_lecture_for_homework'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='lecture_for_homework',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lecture_for_homework', to='Lecture.lecture', verbose_name='Лекция'),
        ),
    ]
