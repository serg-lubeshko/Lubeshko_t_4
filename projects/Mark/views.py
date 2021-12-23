from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from projects.Homework.models import Homework
# from projects.Solution.serializers import HomeworkForSolution
from projects.Mark.serializers import SolutionForProfessorCheckSerializer, MarkSerializer
from projects.Person.models import MyUser
from projects.permission import IsOwnerOrReadOnly


class ProfessorWatchHomework(generics.GenericAPIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = MarkSerializer
    queryset = MyUser.objects.all()

    def get(self, request):
        query = MyUser.objects.filter(user_solution__task_solved='True')
        serializer = SolutionForProfessorCheckSerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid(raise_exception=True):
            # print(request.data)
            serializer.save(user_mark_id=request.user.pk)
            return Response(status=status.HTTP_200_OK)
