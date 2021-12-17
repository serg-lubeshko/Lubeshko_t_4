from django.db.models import Q
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from Course.models import Course, StudCour, TeachCour
from Course.serializer import CourseSerializer, StudCourSerializer, TeachCourSerializer
from Person.models import MyUser
from conf.permission import IsOwnerOrReadOnly


class CourseList(generics.ListAPIView):
    # authentication_classes = [SessionAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    # queryset = Course.objects.all()
    # queryset = StudCour.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        person= MyUser.objects.get(username=self.request.user)
        user_pk = person.pk
        user_status = person.status
        print(user_status)
        if user_status in ('p',):
            return Course.objects.filter(Q(teacher=user_pk) | Q(author_id=user_pk))

        if user_status in ('s',):
            return Course.objects.filter(Q(student=user_pk) | Q(author_id=user_pk))

class DetailCourse(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly ]
    lookup_url_kwarg = 'pk'
    serializer_class = CourseSerializer

    def get_queryset(self):
        person= MyUser.objects.get(username=self.request.user)
        user_pk = person.pk
        user_status = person.status
        if user_status in ('p',):
            return Course.objects.filter(Q(teacher=user_pk) | Q(author_id=user_pk))



