from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from projects.Homework.models import Homework
from projects.Homework.serializers import HomeworkSerializer, LectureFofHomework
from projects.Lecture.models import Lecture
from projects.permission import IsRegisteredPersonHomework


class HomeworkToLecture(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = HomeworkSerializer
    queryset = Homework.objects.all()

    # def get_lecture(self, lecture_id):
    #     return Lecture.objects.filter(id=lecture_id)

    def get(self, request):
        query = Lecture.objects.filter(professor=self.request.user)
        print(query)
        serializer = LectureFofHomework(query, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HomeworkSerializer(data=self.request.data)
        if serializer.is_valid(raise_exception=True):
            print('ddddddddddddddddddddddd')
            serializer.save(professor_id=self.request.user.id)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            # serializer.save(course_id=1, professor_id=self.request.user.id)
            # return Response(status=status.HTTP_200_OK)

# class HomeworkToLecture(generics.ListCreateAPIView):
#     serializer_class = HomeworkSerializer
#
#     def get_queryset(self):
#         user=self.request.user.pk
#         queryset = Homework.objects.filter(professor=self.request.user)
#         return queryset