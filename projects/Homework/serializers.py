from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from projects.Homework.models import Homework
from projects.Lecture.models import Lecture
from projects.Lecture.serializers import LectureSerializer





class HomeworkSerializer(serializers.ModelSerializer):
    a = 1
    professor = serializers.PrimaryKeyRelatedField(read_only=True)
    lecture_for_homework = serializers.ChoiceField(
        choices=[i.id for i in Lecture.objects.filter(professor_id=a)],
        source='lecture_for_homework_id')

    class Meta:
        model = Homework
        fields = ['id', 'title', 'homework_task', 'published_at', 'professor', 'lecture_for_homework']


    def validate_homework_task(self, value):
        a=HomeworkSerializer().user = self.context['request'].user.pk
        user_id = self.context['request'].user.pk
        lecture_id = self.context['request'].data['lecture_for_homework']
        if Homework.objects.filter(professor_id=user_id, lecture_for_homework=lecture_id).count() > 0:
            raise serializers.ValidationError("Вы добавили уже домашнюю работу")
        return value


class LectureFofHomework(LectureSerializer):
    lecture_for_homework = HomeworkSerializer(many=True)

    class Meta:
        model = Lecture
        fields = ['id', 'title', 'lecture_for_homework']
