from django.urls import path

from projects.Solution.views import SolutionToHomework

urlpatterns = [
    # path('add-solution/<int:homework_id>', SolutionToHomework.as_view())
    path('watch-task-and-add-solution/', SolutionToHomework.as_view()),
    # path('watch-homework-professor/', ProfessorWatchHomework.as_view())

]
