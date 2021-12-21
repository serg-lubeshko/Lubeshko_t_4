from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from projects.Course.models import StudCour
from projects.Homework.models import Homework
from projects.Lecture.models import Lecture
from projects.Solution.serializers import HomeworkForSolution, SolutionSerializers
from projects.permission import IsRegisteredStudent


class SolutionToHomework(generics.GenericAPIView):
    permission_classes = [IsAuthenticated, IsRegisteredStudent]
    serializer_class = SolutionSerializers
    queryset = Homework.objects.all()


    def get_lecture(self, homework_id):
        return Homework.objects.get(id=homework_id)

    def get(self, request, homework_id):
        serializer = HomeworkForSolution(self.get_lecture(homework_id))
        return Response(serializer.data)

    def post(self, request, homework_id):
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(homework_solution_id=homework_id, user_solution_id=self.request.user.id)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


