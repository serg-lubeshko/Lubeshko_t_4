from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from projects.Homework.models import Homework
from projects.Homework.serializers import HomeworkSerializer, LectureFofHomework
from projects.Lecture.models import Lecture
from projects.permission import IsRegisteredPersonHomework, IsProffesorOwnerOrReadOnly


class HomeworkToLecture(generics.GenericAPIView):
    permission_classes = [IsAuthenticated, IsProffesorOwnerOrReadOnly]
    serializer_class = HomeworkSerializer
    queryset = Homework.objects.all()

    def get(self, request):
        query = Lecture.objects.filter(professor=self.request.user)
        serializer = LectureFofHomework(query, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HomeworkSerializer(data=self.request.data,
                                        context={'request': request})
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

# class HomeworkToLecture(generics.ListCreateAPIView):
#     serializer_class = HomeworkSerializer
#
#     def get_queryset(self):
#         user=self.request.user.pk
#         queryset = Homework.objects.filter(professor=self.request.user)
#         return queryset
