from django.urls import path

from Course.views import CourseList

urlpatterns = [

    path('all-course/', CourseList.as_view()),


]
