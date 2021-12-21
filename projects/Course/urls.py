from django.urls import path

from projects.Course.views import CourseList, DetailCourse, AddTeacher, AddStudent

urlpatterns = [

    path('all', CourseList.as_view()),
    path('detail/<int:pk>', DetailCourse.as_view()),
    path('add-professor/<int:course_id>', AddTeacher.as_view()),
    path('add-student/<int:course_id>', AddStudent.as_view()),


]
