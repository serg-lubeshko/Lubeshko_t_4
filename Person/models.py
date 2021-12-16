from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):

    class StatusPerson(models.TextChoices):
        Pr = 'p', 'Professor'
        St = 's', 'Student'

    status_ticket = models.CharField(max_length=2,
                                     verbose_name='Статус юзера',
                                     choices=StatusPerson.choices,
                                     default=StatusPerson.Pr)

    # USERNAME_FIELD = 'sername' #это строка, описывающая имя поля в пользовательской модели,
    # которое используется в качестве уникального идентификатора.

    #https: // django.fun / tips / v - chem - raznica - mezhdu - abstractuser - i - abstractbaseuser - v - django /

    # objects = MyUserManager()

    def __str__(self):
        return self.username
