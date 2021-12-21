from django.urls import path

from projects.Course.views import CourseList, DetailCourse,AddTeacher

urlpatterns = [

    path('all', CourseList.as_view()),
    path('detail/<int:pk>', DetailCourse.as_view()),
    path('add-professor/<int:pk>', AddTeacher.as_view()),


]
