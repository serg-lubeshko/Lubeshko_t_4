from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from projects.Mark.models import Mark
from projects.Mark.serializers import SolutionForProfessorCheckSerializer, MarkSerializer, MarkDetailSerializers
from projects.Person.models import MyUser
from projects.permission import IsProfessorOrReadOnlyMark, IsProfessorOrReadOnlyMarkDetail


class ProfessorWatchHomework(generics.GenericAPIView):
    """ Профессор смотрит solution и ставит оценку, может написать коментарий"""

    permission_classes = [IsAuthenticated, IsProfessorOrReadOnlyMark]
    serializer_class = MarkSerializer
    queryset = MyUser.objects.all()

    def get(self, request):
        query = MyUser.objects.filter(user_solution__task_solved='True')
        serializer = SolutionForProfessorCheckSerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=self.request.data,
                                           context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save(user_mark_id=request.user.pk)
            return Response(status=status.HTTP_200_OK)


class ProfessorMarkDetail(generics.RetrieveUpdateAPIView):
    """ Профессор меняет оценку"""

    permission_classes = [IsAuthenticated, IsProfessorOrReadOnlyMarkDetail]
    serializer_class = MarkDetailSerializers
    queryset = Mark.objects.all()
    lookup_field = 'solution_id'


#ДОООООООООООООООБАВИТЬ СООБЩЕНИЯ
#Возможность студента смотреть свои работы
# Студент пишет коментарии
#Permission
#Пересмотреть название полей
#Переделать лекции


#Не понятно как решить проблему с миграциями