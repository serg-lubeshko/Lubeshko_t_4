from django.urls import path

from projects.Person.views import UserRegister

urlpatterns = [

    path('create/', UserRegister.as_view()),


]
