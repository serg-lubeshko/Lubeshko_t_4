from django.urls import path

from Person.views import UserRegister

urlpatterns = [

    path('create/', UserRegister.as_view()),


]
