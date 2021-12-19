from rest_framework import permissions


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


# class ZareginStudent(permissions.BasePermission):
#     def has_permission(self, request, view):
        
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        # return request.user.status == 'p'

# class XXXX(permissions.BasePermission):
#
#     def has_object_permission(self, request, view, obj):
#
#         if request.method in permissions.SAFE_METHODS:
#             return True
#
#         return obj.professor.pk == request.user.pk