from django.db.models import Q
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from Course.models import Course
from Lecture.models import Lecture
from Lecture.serializers import LectureSerializer
from Person.models import MyUser
from conf.permission import IsOwnerOrReadOnly


class LectureList(generics.ListCreateAPIView):
    """Список лекций"""

    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = LectureSerializer

    def get_queryset(self):
        # person = MyUser.objects.get(username=self.request.user)
        # user_pk = person.pk
        # user_status = person.status
        user = self.request.user
        print(user.pk)
        if user.status in ('p',):
            return Lecture.objects.filter(course__author=user.pk)


    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)
