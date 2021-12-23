from django.db import models

from projects.Person.models import MyUser
from projects.Solution.models import Solution


class Mark(models.Model):
    mark = models.SmallIntegerField(verbose_name='Оценка')
    solution = models.OneToOneField(Solution, verbose_name='Решение', related_name='mark', blank=True, null=True,
                                    on_delete=models.CASCADE)
    user_mark = models.ForeignKey(MyUser, related_name='user_mark', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.mark} | {self.solution}'