from rest_framework import serializers

from Course.serializer import CourseSerializer
from Lecture.models import Lecture
from Person.serializers import UserSerializer


class LectureSerializer(serializers.ModelSerializer):
    """>>>   """


    professor = UserSerializer(read_only=True)
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Lecture
        fields = ['id', 'title', 'file_present', 'published_at', 'professor', 'course']