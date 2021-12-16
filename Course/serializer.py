from rest_framework import serializers

from Course.models import Course, StudCour, TeachCour
from Person.serializers import UserSerializer


class CourseSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Course
        fields = ['id', 'author', 'name', 'description', 'published_at']


class StudCourSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = StudCour
        fields = ['id', 'student', 'course']


class TeachCourSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = TeachCour
        fields = ['id', 'teacher', 'course']
