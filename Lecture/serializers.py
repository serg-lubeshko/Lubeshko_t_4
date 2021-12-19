from rest_framework import serializers

from Course.models import Course
from Course.serializer import CourseSerializer
from Lecture.models import Lecture
from Person.serializers import UserSerializer


class LectureSerializer(serializers.ModelSerializer):
    """>>> LectureToCourse >>>  LectureRUD """

    professor = UserSerializer(read_only=True)
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Lecture
        fields = ['id', 'title', 'file_present', 'published_at', 'professor', 'course']


# class Lecture2Serializer(serializers.ModelSerializer):
#     """>>>   """
#
#
#     professor = UserSerializer(read_only=True)
#     # course = CourseSerializer(read_only=True)
#
#     class Meta:
#         model = Lecture
#         fields = ['id', 'title', 'file_present', 'published_at', 'professor']


class CourseLectureSerializer(serializers.ModelSerializer):
    ''' >>> LectureToCourse '''

    lectures=serializers.StringRelatedField(many=True, read_only=True)
    # course=serializers.Lecture2Serializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id','name','lectures']
            