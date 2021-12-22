from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from projects.Homework.models import Homework
from projects.Lecture.models import Lecture
from projects.Lecture.serializers import LectureSerializer


class HomeworkSerializer(serializers.ModelSerializer):
    # Сделать свои проверки !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! На уникальность и на то что профессор не приглашенный не может
    professor = serializers.PrimaryKeyRelatedField(read_only=True)
    lecture_for_homework = serializers.ChoiceField(
        choices=[i.id for i in Lecture.objects.filter(professor_id=1)], source='lecture_for_homework_id')

    class Meta:
        model = Homework
        # fields = ['id', 'title', 'homework_task', 'published_at', 'professor', 'lecture_for_homework'] ПЕРЕДЕЛАТЬ ВАЛИД НЕ РАБОТАЕТ ПРИ READONLY
        fields = ['id', 'title', 'homework_task', 'published_at', 'professor', 'lecture_for_homework']
        # fields = ['id', 'title', 'homework_task', 'published_at']
        # validators = [UniqueTogetherValidator(
        #     queryset=Homework.objects.all(),
        #     fields=['professor', 'lecture_for_homework'],
        #     message='Этот профессор добавил домашнее задание')]



    def validate_homework_task(self, value):
        print(self.context)
        return value
        # if value in Course.objects.filter(professors=request.user):
        #     return value
        # else:
        #     raise serializers.ValidationError("You are not a Professor in this course.")


class LectureFofHomework(LectureSerializer):
    lecture_for_homework = HomeworkSerializer(many=True)

    class Meta:
        model = Lecture
        # fields = ['id', 'title']
        fields = ['id', 'title', 'lecture_for_homework']
