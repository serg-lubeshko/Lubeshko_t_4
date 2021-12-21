from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from projects.Homework.models import Homework
from projects.Lecture.models import Lecture
from projects.Lecture.serializers import LectureSerializer


class HomeworkSerializer(serializers.ModelSerializer):

     #Сделать свои проверки !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! На уникальность и на то что профессор не приглашенный не может
    # professor = serializers.PrimaryKeyRelatedField(read_only=True, default='None')
    # lecture_for_homework = serializers.PrimaryKeyRelatedField(read_only=True, default='None')

    class Meta:
        model = Homework
        # fields = ['id', 'title', 'homework_task', 'published_at', 'professor', 'lecture_for_homework'] ПЕРЕДЕЛАТЬ ВАЛИД НЕ РАБОТАЕТ ПРИ READONLY
        fields = ['id', 'title', 'homework_task', 'published_at']
        # fields = ['id', 'title', 'homework_task', 'published_at']
        # validators = [UniqueTogetherValidator(
        #     queryset=Homework.objects.all(),
        #     fields=['professor', 'lecture_for_homework'],
        #     message='Этот профессор добавил домашнее задание')]


class LectureFofHomework(LectureSerializer):
    lecture_for_homework = HomeworkSerializer(many=True, read_only=True)

    class Meta:
        model = Lecture
        fields = ['id', 'title', 'lecture_for_homework']


