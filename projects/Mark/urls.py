from django.urls import path

from projects.Mark.views import ProfessorWatchHomework, ProfessorMarkDetail

urlpatterns = [

    path('professor-watch-homework-add-mark-message/', ProfessorWatchHomework.as_view()),
    path('professor-update-mark/<int:solution_id>', ProfessorMarkDetail.as_view()),


]