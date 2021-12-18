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


class TeachAddSerializer(serializers.ModelSerializer):
    """ >>> AddTeacher """

    # teacher = UserSerializer()

    class Meta:
        model = TeachCour
        fields = ['teacher', 'course']


class CoursesProfessorsSerializer(serializers.ModelSerializer):

    teacher = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['teacher']



class AddTeacherSerializer(serializers.Serializer):
    """ >>>  AddTeacher """

    teacher = serializers.ChoiceField(choices=[i.username for i in MyUser.objects.filter(status='p')])

    class Meta:
        fields = ['teacher']


class AddStudentSerializer(serializers.Serializer):
    """ >>>    """

    teacher = serializers.ChoiceField(choices=[i.username for i in MyUser.objects.filter(status='p')])

    class Meta:
        fields = ['teacher']
