from rest_framework import serializers

from projects.Mark.models import Mark, MessageTeacher
from projects.Person.models import MyUser
from projects.Solution.models import Solution
from projects.Solution.serializers import SolutionSerializers


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageTeacher
        fields = ['text']


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
        MessageTeacher.objects.create(**instance)
        return validated_data

    def validate(self, data):
        user_id = self.context['request'].user.pk
        solutions_id = self.context['request'].data['solution_id']
        data_dict = dict(data)
        if Mark.objects.filter(user_mark_id=user_id, solution_id=solutions_id).count() > 0:
            raise serializers.ValidationError("Оценка уже добавлен")

class SolutionForProfessorCheckSerializer(serializers.ModelSerializer):
    id_user = serializers.IntegerField(source='id', read_only=True)
    user_solution = SolutionSerializers(many=True)

    class Meta:
        model = MyUser
        fields = ['id_user', 'username', 'user_solution', ]
