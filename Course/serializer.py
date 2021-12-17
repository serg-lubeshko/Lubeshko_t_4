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

    # def _is_my_find(self, obj):
    #     prof = MyUser.objects.filter(status='p')
    #     return prof


# class TeacherCourSerializer(serializers.Serializer):
#     # author = UserSerializer(read_only=True)
#     # new = serializers.ChoiceField(choices=[i.username for i in MyUser.objects.all()])
#     color = serializers.ChoiceField(choices=['red', 'green', 'blue'])
#
#     class Meta:
#         # model = Course
#         fields = ['new', 'color']

class CoursesProfessorsSerializer(serializers.ModelSerializer):

    teacher = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['teacher']



class AddP(serializers.Serializer):
    """>>>  CourseList  >>> DetailCourse"""


    # author = UserSerializer(read_only=True)
    color = serializers.ChoiceField(choices=[i.username for i in MyUser.objects.filter(status='p')])



    class Meta:
        # model = Course
        fields = ['colour']
    