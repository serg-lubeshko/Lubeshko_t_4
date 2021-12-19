from django.db import models

from Course.models import Course
from Lecture.models import Lecture
from Person.models import MyUser


class Homework(models.Model):
    """ Модель курсов """

    homework_task = models.TextField(verbose_name='Домашняя работа')
    title = models.CharField(verbose_name='Название домашней работы', max_length=155)
    published_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')

    professor = models.ForeignKey(MyUser, related_name='professor_lec', verbose_name='Автор лекции',
                                  on_delete=models.CASCADE)

    lecture_for_homework = models.ForeignKey(Lecture, related_name='lecture_for_homework', verbose_name='Лекция', on_delete=models.CASCADE, )

    def __str__(self):
        return f"{self.title} - автор {self.professor}"