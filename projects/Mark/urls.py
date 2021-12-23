from django.urls import path

from projects.Mark.views import ProfessorWatchHomework

urlpatterns = [

    path('professor-watch-homework/', ProfessorWatchHomework.as_view()),


]