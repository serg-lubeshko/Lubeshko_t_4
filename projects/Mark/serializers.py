from rest_framework import serializers

from projects.Mark.models import Mark, MessageTeacher
from projects.Person.models import MyUser
from projects.Solution.models import Solution
from projects.Solution.serializers import SolutionSerializers


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageTeacher
        fields = ['id', 'text']


class MarkSerializer(serializers.ModelSerializer):
    solution_id = serializers.ChoiceField(choices=[i.id for i in Solution.objects.all()])
    mark_message = MessageSerializer()
    mark = serializers.IntegerField(min_value=0, max_value=10)

    class Meta:
        model = Mark
        fields = ['mark', 'solution_id', 'mark_message']

    def create(self, validated_data):
        message = dict(validated_data.pop('mark_message'))
        mark_id = (Mark.objects.create(**validated_data)).pk
        instance = message | {'mark_message_id': mark_id}
        return MessageTeacher.objects.create(**instance)


class SolutionForProfessorCheckSerializer(serializers.ModelSerializer):
    id_user = serializers.IntegerField(source='id', read_only=True)
    user_solution = SolutionSerializers(many=True)

    class Meta:
        model = MyUser
        fields = ['id_user', 'username', 'user_solution', ]


class MarkDetailSerializers(serializers.ModelSerializer):
    message_professor = MessageSerializer(read_only=True, many=True, source='mark_message')

    class Meta:
        model = Mark
        fields = ['mark', 'solution_id', 'message_professor']


# class TextDetailSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = MessageTeacher
#         fields = ['text', 'mark_message']