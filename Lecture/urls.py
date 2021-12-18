from django.urls import path

from Lecture.views import LectureList

urlpatterns = [

    path('all', LectureList.as_view()),



]
