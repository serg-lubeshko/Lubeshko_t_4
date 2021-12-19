from django.urls import path

from Homework.views import HomeworkToLecture

urlpatterns = [

    path('add/<int:lecture_id>', HomeworkToLecture.as_view()),
    # path('all/', HomeworkToLecture.as_view()),
    # path('rud/<int:id>', HomeworkRUD.as_view()),



]
