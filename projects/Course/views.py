from django.db.models import Q
from rest_framework import generics, status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from projects.Course.models import Course, TeachCour, StudCour
from projects.Course.serializers import CourseSerializer, AddTeacherSerializer, AddStudentSerializer
from projects.Person.models import MyUser
from projects.conf.functions_app.Check import CheckCourse
from projects.conf.functions_app.get_object_or_None import get_object_or_None
from projects.permission import IsOwnerOrReadOnly, IsProfessorOrReadOnly


class CourseList(generics.ListCreateAPIView):
    """Список своих курсов и приглашенных, а также добавление нового курса"""

    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly, IsProfessorOrReadOnly]
    serializer_class = CourseSerializer

    def get_queryset(self):
        person = MyUser.objects.get(username=self.request.user)
        user_pk = person.pk
        user_status = person.status
        if user_status in ('p',):
            return Course.objects.filter(teacher=user_pk)

        if user_status in ('s',):
            return Course.objects.filter(student=user_pk)

    def perform_create(self, serializer):
        course_object=serializer.save(author=self.request.user)
        TeachCour.objects.create(course_id=course_object.id, teacher_id=course_object.author_id)


class DetailCourse(generics.RetrieveUpdateDestroyAPIView):
    "Detail могут смотреть студенты и профессора свой курс, владельцы вносить изменения"

    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly, IsProfessorOrReadOnly]
    serializer_class = CourseSerializer

    def get_queryset(self):
        person = MyUser.objects.get(username=self.request.user)
        user_pk = person.pk
        user_status = person.status
        if user_status in ('p',):
            return Course.objects.filter(Q(teacher=user_pk) | Q(author_id=user_pk))


class AddTeacher(GenericAPIView):
    """ Добавляет профессора на курс и делает проверки (есть владелец  курса,
    не добавлен ли повторно)
    """

    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly, IsProfessorOrReadOnly]
    serializer_class = AddTeacherSerializer

    def get(self, request, course_id):
        try:
            quer = Course.objects.get(id=course_id)
            serializer = CourseSerializer(quer)
            return Response(serializer.data)
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    # def get_teacher_query(self, username):
    #     return get_object_or_None(MyUser, username=username)

    def post(self, request, course_id):
        check = CheckCourse(course_id, request.data['teacher']).get_professor()  # Название подумать
        if check is None:
            serializer = self.serializer_class(data=request.data)
            teacher_pk = MyUser.objects.filter(username=request.data['teacher'])[0].pk
            if serializer.is_valid(raise_exception=True) and teacher_pk:
                TeachCour.objects.create(course_id=course_id, teacher_id=teacher_pk)
                return Response(status=status.HTTP_201_CREATED)
        else:
            return Response({
                "userMessage": check,
            },
                status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )


class AddStudent(GenericAPIView):
    """ Добавляет студента     """

    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly, IsProfessorOrReadOnly]
    # queryset = Course.objects.all()
    serializer_class = AddStudentSerializer

    def get(self, request, course_id):
        try:
            quer = Course.objects.get(id=course_id)
            serializer = CourseSerializer(quer)
            return Response(serializer.data)
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    # def get_teacher_query(self, username):
    #     return get_object_or_None(MyUser, username=username)

    def post(self, request, course_id):

        check = CheckCourse(course_id, request.data['student']).get_student()
        if check is None:
            serializer = self.serializer_class(data=request.data)
            student_pk = MyUser.objects.filter(username=request.data['student'])[0].pk
            if serializer.is_valid() and student_pk:
                StudCour.objects.create(course_id=course_id, student_id=student_pk)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({
                "userMessage": check,
            },
                status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )
