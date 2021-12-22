from rest_framework import serializers

from projects.Course.models import Course
from projects.Course.serializers import CourseSerializer
from projects.Lecture.models import Lecture
from projects.Person.serializers import UserSerializer


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

    # lectures=serializers.StringRelatedField(many=True, read_only=True)
    lectures=LectureSerializer(many=True, read_only=True)
    name_course = serializers.CharField(source='name')
    # course=serializers.Lecture2Serializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = [ 'name_course','lectures']
            