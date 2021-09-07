import copy


class User:
    pass


class Teacher(User):
    pass


class Student(User):
    pass


class UserFactory:
    users = {
        'student': Student,
        'teacher': Teacher,
    }

    @classmethod
    def create_user(cls, type):
        return cls.users[type]()


class CourseProt:
    def clone(self):
        return copy.deepcopy(self)


class Course(CourseProt):

    def __init__(self, name, category):
        self.name = name
        self.category = category
        # self.category.courses.append(self)


class OnlineCourse(Course):
    pass


class OfflineCourse(Course):
    pass


class CourseFactory:
    types = {
        'online': OnlineCourse,
        'offline': OfflineCourse
    }

    @classmethod
    def create_course(cls, type, name, category):
        return cls.types[type](name,category)


class Category:
    id = 1

    def __init__(self, name, category):
        self.id = Category.id
        Category.id += 1
        self.name = name
        self.category = category
        self.courses = []


class Engine:
    def __init__(self):
        self.teachers = []
        self.students = []
        self.courses = []
        self.categories = []

    @staticmethod
    def create_user(type):
        return UserFactory.create_user(type)

    @staticmethod
    def create_category(name, category=None):
        return Category(name, category)

    @staticmethod
    def create_course(type, name, category):
        return CourseFactory.create_course(type, name, category)


class Singleton(type):

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls.__instance = {}

    def __call__(cls, *args, **kwargs):
        if args:
            name = args[0]
        if kwargs:
            name = kwargs['name']
        if name in cls.__instance:
            return cls.__instance[name]
        else:
            cls.__instance[name] = super().__call__(*args, **kwargs)
            return cls.__instance[name]

class Loger(metaclass=Singleton):
    def __init__(self, name):
        self.name = name

    @staticmethod
    def log(text):
        print(f'Logger: {text}')
