from django.urls import path

from projects.Person.views import UserRegister

urlpatterns = [

    path('create-person/', UserRegister.as_view()),


]
