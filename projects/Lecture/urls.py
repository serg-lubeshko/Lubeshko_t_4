from django.urls import path

# from Lecture.views import LectureList
from projects.Lecture.views import LectureToCourse, LectureRUD

urlpatterns = [

    # path('all', LectureList.as_view()),
    path('add/<int:course_id>', LectureToCourse.as_view()),
    path('rud/<int:id>', LectureRUD.as_view()),



]
