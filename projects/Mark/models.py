from django.db import models

from projects.Person.models import MyUser
from projects.Solution.models import Solution


class Mark(models.Model):
    mark = models.SmallIntegerField(verbose_name='Оценка')
    solution = models.OneToOneField(Solution, verbose_name='Решение', related_name='mark_solution', blank=True,
                                    null=True,
                                    on_delete=models.CASCADE)
    user_mark = models.ForeignKey(MyUser, related_name='user_mark', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.mark} | {self.solution}'


class MessageTeacher(models.Model):
    text = models.TextField(blank=False, null=True, verbose_name='Текстовое сообщение')
    # user_message = models.ForeignKey(MyUser, verbose_name='Сообщение написал', on_delete=models.CASCADE)
    mark_message = models.ForeignKey(Mark, verbose_name='Оценка_ID', on_delete=models.CASCADE,
                                     related_name='mark_message')

    published_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')

    def __str__(self):
        return f'Сообщение текстовое № {self.id}'
