from django.urls import path

from Person.views import UserRegister

urlpatterns = [

    path('register/', UserRegister.as_view()),


]
