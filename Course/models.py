from django.db import models

from Person.models import MyUser


class Course(models.Model):
    """
    
    CRUD своих курсов
    Просмотр доступных курсов
    
    Добавление/Удаление студента к своему курсу  - создать поле
    Добавление нового преподавателя к своему курсу  создать поле + на самого препода = 2 поля
    (у одного курса много преподов, как и препода много курсов м2м
    """
    name = models.CharField(max_length=255, verbose_name='Название курса')
    description = models.TextField(verbose_name='Описание', blank=True)
    published_at = models.DateField(auto_now_add=True, verbose_name='Опубликовано')
    author = models.ForeignKey(MyUser, related_name='author_user', verbose_name='автор курса', on_delete=models.CASCADE)
    student = models.ManyToManyField(MyUser, related_name='student_user', verbose_name='студент курса',
                                     through='StudCour', )
    teacher = models.ManyToManyField(MyUser, related_name='teacher_user', verbose_name='соавтор курса',
                                     through='TeachCour', )

    def __str__(self):
        return f"{self.name}|{self.author}"


class StudCour(models.Model):
    student = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course}|{self.student}"


class TeachCour(models.Model):
    teacher = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course}|{self.teacher}"
