from django.db import models

from Homework.models import Homework
from Person.models import MyUser


class Solution(models.Model):
    """ Модель решения задачи"""

    solution_task = models.URLField(verbose_name='Решение')
    user_solution = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='user_solution',
                                      verbose_name='Студент')
    homework_solution = models.ForeignKey(Homework, on_delete=models.CASCADE, related_name='homework_solution',
                                             verbose_name='Домашняя работа')
    mark = models.SmallIntegerField(verbose_name='Оценка', blank=True, null=True)
    task_solved = models.BooleanField(verbose_name='Задача решена?')

    def __str__(self):
        return f'{self.solution_task} - {self.homework_solution}'
