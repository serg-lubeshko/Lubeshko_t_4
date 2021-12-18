from django.db.models import Q
from rest_framework import generics, status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from Course.models import Course, TeachCour
from Course.serializer import CourseSerializer, AddTeacherSerializer
from Person.models import MyUser
from conf.functions_app.Check import CheckCourse
from conf.functions_app.get_object_or_None import get_object_or_None
from conf.permission import IsOwnerOrReadOnly, IsProfessorOrReadOnly


class CourseList(generics.ListCreateAPIView):
    """Список своих курсов и приглашенных, а также добавление нового"""

    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = CourseSerializer

    def get_queryset(self):
        person = MyUser.objects.get(username=self.request.user)
        user_pk = person.pk
        user_status = person.status
        if user_status in ('p',):
            return Course.objects.filter(Q(teacher=user_pk) | Q(author_id=user_pk))

        if user_status in ('s',):
            return Course.objects.filter(Q(student=user_pk) | Q(author_id=user_pk))

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class DetailCourse(generics.RetrieveUpdateDestroyAPIView):
    "Могут смотреть студенты и профессора свой курс"

    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = CourseSerializer

    def get_queryset(self):
        person = MyUser.objects.get(username=self.request.user)
        user_pk = person.pk
        user_status = person.status
        if user_status in ('p',):
            return Course.objects.filter(Q(teacher=user_pk) | Q(author_id=user_pk))


class AddTeacher(GenericAPIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly, IsProfessorOrReadOnly]

    queryset = Course.objects.all()
    serializer_class = AddTeacherSerializer

    def get(self, request, pk):
        quer = Course.objects.get(id=pk)
        serializer = CourseSerializer(quer)
        return Response(serializer.data)

    def check_username(self, username):
        return get_object_or_None(MyUser, username=username)

    def post(self, request, pk):

        check = CheckCourse(pk, request.data['teacher']).get_professor()
        if check is None:
            # CheckCourse(pk, 'admin', request).check_course()
            serializer = self.serializer_class(data=request.data)
            teacher_pk = self.check_username(request.data['teacher'])
            if serializer.is_valid() and teacher_pk:
                TeachCour.objects.create(course_id=pk, teacher_id=teacher_pk.pk)
                return Response(status=status.HTTP_201_CREATED)
        else:
            return Response({
                "userMessage": check,
            },
                status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )

# class AddTeacher(views.APIView):
#     ''' Добавить препода????????????????'''
#
#     # permission_classes = [IsAuthenticated, IsOwnerOrReadOnly ]
#     # serializer_class = TeachCourSerializer
#
#     # def get(self, request,pk):
#     #     # query= Course.objects.get(id=pk)
#     #     # serializer = TeacherAddSerializer(query)
#     #     data = Course.objects.get(pk=pk)
#     #     serializer = TeacherAddSerializer(data)
#     #
#     #     return Response ({'course': serializer.data})
#
#
#     def post(self, request):
#         serializer = TeacherAddSerializer()
#         # course = TeachCour.objects.all()
#         return Response(status=status.HTTP_201_CREATED)
#
#     # def get(self,*args,**kwargs):
#     #     query = Course.objects.get(id=8)
#     #     serializer = CourseSerializer(query)
#     #     return Response(serializer.data)
#
#     # def post(self):
#     #     serializer = TeachCourSerializer
#     #     if serializer.is_valid():
#     #         # serializer.save()
#     #         return Response(status=status.HTTP_201_CREATED)
#
