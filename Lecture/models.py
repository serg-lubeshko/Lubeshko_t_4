from django.db import models

from Course.models import Course
from Person.models import MyUser


class Lecture(models.Model):
    """ Модель курсов """

    title = models.CharField(max_length=255, verbose_name='Название лекции')
    file_present = models.FileField(upload_to='files/%Y/%m/%d/', blank=True, verbose_name="Презентация")
    published_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')

    professor = models.ForeignKey(MyUser, related_name='professor', verbose_name='Автор лекции',
                                  on_delete=models.CASCADE)

    course = models.ForeignKey(Course, related_name='course', verbose_name='Курсс', on_delete=models.CASCADE, )

    def __str__(self):
        return f"{self.title} - автор {self.professor}"
