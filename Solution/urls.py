from django.urls import path

from Solution.views import SolutionToHomework

urlpatterns = [

    path('add/<int:homework_id>', SolutionToHomework.as_view()),


]
