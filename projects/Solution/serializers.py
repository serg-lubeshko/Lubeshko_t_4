from rest_framework import serializers

from projects.Homework.models import Homework
from projects.Lecture.serializers import LectureSerializer
from projects.Solution.models import Solution


class SolutionSerializers(serializers.ModelSerializer):
    homework_solution = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Solution
        fields = ['id', 'task_solved', 'solution_task', 'homework_solution']
        # read_only_field = ('homework_solution',)


class HomeworkForSolution(serializers.ModelSerializer):
    lecture_for_homework = LectureSerializer()
    # title = serializers.CharField(read_only=True)

    class Meta:
        model = Homework
        fields = ['id', 'title', 'homework_task', 'lecture_for_homework']
