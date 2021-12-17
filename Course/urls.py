from django.urls import path

from Course.views import CourseList, DetailCourse

urlpatterns = [

    path('all-course/', CourseList.as_view()),
    path('detail/<int:pk>', DetailCourse.as_view()),


]
