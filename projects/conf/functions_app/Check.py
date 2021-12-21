from projects.Course.models import Course, TeachCour
from projects.Person.models import MyUser
from projects.conf.functions_app.get_object_or_None import get_object_or_None


class CheckCourse:
    def __init__(self, course: id, username: str):
        self.course = course
        self.username = username

    def check_course(self):
        "Есть ли курс"

        course = Course.objects.filter(pk=self.course).exists()
        if not course:
            return "Такого курса нет"
        return None

    def get_professor(self):
        "Проверка профессора"

        user = get_object_or_None(MyUser, username=self.username)
        if user != None and user.status == 'p':
            user_id = user.pk
            owner = Course.objects.get(id=self.course).author_id
            if owner == user_id:
                return "Сам себя на курс профессор не может добавить"
            if TeachCour.objects.filter(course_id=self.course).filter(teacher_id=user_id):
                return "Профессор уже добавлен"
            return self.check_course()
        return "Такого профессора нет"
