from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from Course.models import Course, StudCour, TeachCour
from Person.models import MyUser
from Person.serializers import UserSerializer


class CourseSerializer(serializers.ModelSerializer):
    """>>>  CourseList  >>> DetailCourse"""


    author = UserSerializer(read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'author', 'name', 'description', 'published_at', 'update_at']


class StudCourSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = StudCour
        fields = ['id', 'student', 'course']


class TeachCourSerializer(serializers.ModelSerializer):
    """ >>> AddTeacher """

    teacher = UserSerializer(many=True)

    class Meta:
        model = Course
        fields = ['teacher',]

    # def _is_my_find(self, obj):
    #     prof = MyUser.objects.filter(status='p')
    #     return prof


class TeacherAddSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    teacher = UserSerializer()

    class Meta:
        model = Course
        fields = ['id', 'author', 'name', 'description', 'published_at', 'update_at', 'teacher']
