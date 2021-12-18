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



class AddTeacherSerializer(serializers.Serializer):
    """>>>  CourseList  >>> DetailCourse"""


    # author = UserSerializer(read_only=True)
    teacher = serializers.ChoiceField(choices=[i.username for i in MyUser.objects.filter(status='p')])
    # course_id= serializers.IntegerField(read_only=True)



    class Meta:
        # model = Course
        fields = ['teacher']

        def validate_teacher(self, data):
            """
            Check that start is before finish.
            """
            if data['teacher'] == 'puser2':
                print(data)
                raise serializers.ValidationError("finish must occur after start")
            return data
        

        # return  TeachCour.objects.create(**validatted_data)