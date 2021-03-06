# Generated by Django 4.0 on 2021-12-21 08:20 (переделал все, в старые миграции не видели Person)

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Course', '0001_initial'),
        ('Person', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название лекции')),
                ('file_present', models.FileField(blank=True, upload_to='files/%Y/%m/%d/', verbose_name='Презентация')),
                ('published_at', models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lectures', to='Course.course', verbose_name='Курс')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='professor', to='Person.myuser', verbose_name='Автор лекции')),
            ],
        ),
    ]
