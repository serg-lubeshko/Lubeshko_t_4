from projects.Course.models import Course, TeachCour
from projects.Person.models import MyUser
from projects.conf.functions_app.get_object_or_None import get_object_or_None


class CheckCourse:
    def __init__(self, course: id, username: str):
        self.course = course
        self.username = username

    def check_course(self):
        "Есть ли курс"

        return get_object_or_None(Course, pk=self.course)

    def get_professor(self):
        """  Проверка профессора добавлении на курс"""

        user = get_object_or_None(MyUser, username=self.username)
        if user is None or user.status != 'p':
            return "Такой пользователь не может быть добавлен"
        course = self.check_course()
        if course is None:
            return "Такого курса нет"
        user_id = user.pk
        if course.author_id == user_id:
            return "Сам себя на курс профессор не может добавить"
        if TeachCour.objects.filter(course_id=self.course).filter(teacher_id=user_id):
            return "Профессор уже добавлен"
        return None
