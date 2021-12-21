from django.db import models

from django.db import models

from projects.Person.models import MyUser


class Course(models.Model):
    """ Модель курсов """

    name = models.CharField(max_length=255, verbose_name='Название курса')
    description = models.TextField(verbose_name='Описание', blank=True)
    published_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Последние изменения')
    author = models.ForeignKey(MyUser, related_name='author_user', verbose_name='автор курса', on_delete=models.CASCADE)
    student = models.ManyToManyField(MyUser, related_name='student', verbose_name='студент курса',
                                     through='StudCour', )
    teacher = models.ManyToManyField(MyUser, related_name='teacher', verbose_name='соавтор курса',
                                     through='TeachCour', )

    def __str__(self):
        return f"{self.name}|{self.author}"


class StudCour(models.Model):
    student = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course}|{self.student}"


class TeachCour(models.Model):
    teacher = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='tea')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='cou')

    def __str__(self):
        return f"{self.course}|{self.teacher}"
