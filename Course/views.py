from django.db.models import Q
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from Course.models import Course, StudCour, TeachCour
from Course.serializer import CourseSerializer, StudCourSerializer, TeachCourSerializer
from Person.models import MyUser


class CourseList(generics.ListAPIView):
    # authentication_classes = [SessionAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    # queryset = Course.objects.all()
    # queryset = StudCour.objects.all()
    serializer_class = TeachCourSerializer

    def get_queryset(self):
        person= MyUser.objects.get(username=self.request.user)
        user_pk = person.pk
        user_status = person.status
        if user_status in ('p',):
            return TeachCour.objects.filter(Q(teacher_id=user_pk)|Q(course__author_id=user_pk))
            # return Course.objects.filter(Q(author_id=user_pk)|Q()

        
