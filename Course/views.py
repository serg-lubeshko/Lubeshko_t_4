from django.db.models import Q
from django.shortcuts import render
from rest_framework import generics, views, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from Course.models import Course, StudCour, TeachCour
from Course.serializer import CourseSerializer, StudCourSerializer, TeachCourSerializer, TeacherAddSerializer
from Person.models import MyUser
from Person.serializers import UserSerializer
from conf.permission import IsOwnerOrReadOnly


class CourseList(generics.ListCreateAPIView):
    """Список своих курсов и приглашенных, а также добавление нового"""
    # authentication_classes = [SessionAuthentication, ]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly ]
    serializer_class = CourseSerializer

    def get_queryset(self):
        person= MyUser.objects.get(username=self.request.user)
        user_pk = person.pk
        user_status = person.status
        if user_status in ('p',):
            return Course.objects.filter(Q(teacher=user_pk) | Q(author_id=user_pk))

        if user_status in ('s',):
            return Course.objects.filter(Q(student=user_pk) | Q(author_id=user_pk))

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



class DetailCourse(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly ]
    serializer_class = CourseSerializer

    def get_queryset(self):
        person= MyUser.objects.get(username=self.request.user)
        user_pk = person.pk
        user_status = person.status
        if user_status in ('p',):
            return Course.objects.filter(Q(teacher=user_pk) | Q(author_id=user_pk))


class AddTeacher(views.APIView):
    ''' Добавить препода'''

    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly ]
    serializer_class = TeachCourSerializer


    def post(self, request):
        # serializer = TeachCourSerializer(request.data)
        # course = TeachCour.objects.all()
        return Response(status=status.HTTP_201_CREATED)

    # def get(self,*args,**kwargs):
    #     query = Course.objects.get(id=8)
    #     serializer = CourseSerializer(query)
    #     return Response(serializer.data)

    # def post(self):
    #     serializer = TeachCourSerializer
    #     if serializer.is_valid():
    #         # serializer.save()
    #         return Response(status=status.HTTP_201_CREATED)

