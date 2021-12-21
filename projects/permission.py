from rest_framework import permissions

from projects.Course.models import Course, StudCour
from projects.Homework.models import Homework
from projects.Lecture.models import Lecture


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user

class IsProfessorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        print( 'eddedede')
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.status == 'p'


class IsProffesorOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.professor.pk == request.user.pk


class IsRegisteredStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            param = request.parser_context['kwargs'].get('homework_id')
            id_lecture = Homework.objects.get(id=param).lecture_for_homework_id
            id_course =Lecture.objects.get(id=id_lecture).course_id
            user = request.user.pk
            return StudCour.objects.filter(course_id=id_course).filter(student_id=user)
        except Homework.DoesNotExist:
            return False


# class XXXX(permissions.BasePermission):
#
#     def has_object_permission(self, request, view, obj):
#
#         if request.method in permissions.SAFE_METHODS:
#             return True
#
#         return obj.professor.pk == request.user.pk