from django.urls import path

from projects.Homework.views import HomeworkToLecture

urlpatterns = [

    path('add-homework/', HomeworkToLecture.as_view()),
    # path('all/', HomeworkToLecture.as_view()),
    # path('rud/<int:id>', HomeworkRUD.as_view()),



]
