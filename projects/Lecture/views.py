from rest_framework import status, generics
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from projects.Course.models import Course
from projects.Lecture.models import Lecture
from projects.Lecture.serializers import LectureSerializer, CourseLectureSerializer
from projects.permission import IsProfessorOrReadOnly, IsProffesorOwnerOrReadOnly


class LectureToCourse(GenericAPIView):
    """Список лекций к курсу может добавить профессор. ????? Подумать над приглашенным"""

    permission_classes = [IsAuthenticated, IsProfessorOrReadOnly]
    serializer_class = LectureSerializer
    parser_classes = (FormParser, MultiPartParser)

    def get(self, request, course_id):
        quer = Course.objects.get(id=course_id)
        serializer = CourseLectureSerializer(quer)
        return Response(serializer.data)

    def post(self, request, course_id):
        serializer = LectureSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save(course_id=course_id, professor_id=self.request.user.id)  #ПООООМЕНЯТЬ ID
            return Response(status=status.HTTP_200_OK)

    # def perform_create(self, serializer):
    #     serializer.save(course_id=1, professor_id=self.request.user.pk)


class LectureRUD(generics.RetrieveUpdateDestroyAPIView):
    """ Обновление, удаление лекции. Может только автор лекции """

    permission_classes = [IsAuthenticated,IsProffesorOwnerOrReadOnly]
    serializer_class = LectureSerializer
    queryset = Lecture.objects.all()
    lookup_field = 'id'                      #id лекции
