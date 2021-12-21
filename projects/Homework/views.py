from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from projects.Homework.models import Homework
from projects.Homework.serializers import HomeworkSerializer, LectureFofHomework
from projects.Lecture.models import Lecture
from projects.permission import IsProfessorOrReadOnly


class HomeworkToLecture(generics.GenericAPIView):
    permission_classes = [IsAuthenticated, IsProfessorOrReadOnly]
    serializer_class = HomeworkSerializer
    queryset = Homework.objects.all()

    def get_lecture(self, lecture_id):
        return Lecture.objects.get(id=lecture_id)

    def get(self, request, lecture_id):
        serializer = LectureFofHomework(self.get_lecture(lecture_id))
        return Response(serializer.data)

    def post(self, request, lecture_id):
        serializer = HomeworkSerializer(data=self.request.data)
        if serializer.is_valid():
            # serializer.save(lecture_for_homework=self.get_lecture(lecture_id), professor_id=self.request.user.id)

            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            # serializer.save(course_id=1, professor_id=self.request.user.id)
            # return Response(status=status.HTTP_200_OK)
