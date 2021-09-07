from my_framework.templator import render
from pattenrs.creation_patterns import Engine, Loger

site = Engine()
logger = Loger('log')


def index_view(request):
    page = 'index.html'
    template = render(page, param='Test param')
    return '200 OK', [template.encode(encoding='utf-8')]


def about_view(request):
    return '200 OK', [b'About']


def not_found_view(request):
    return '404 PNF', [b'Page not found...']


class Other:
    def __call__(self, request):
        return '200 OK', [b'Other']


class Contacts:
    def __call__(self, request):
        page = 'contacts.html'
        template = render(page)
        if request['method'] == "POST":
            print(f'Получили данные с формы: {request["data"]}')
        return '200 OK', [template.encode(encoding='utf-8')]

class CourseList:
    def __call__(self, *args, **kwargs):
        page = 'courses.html'
        courses = site.courses
        print(courses)
        template = render(page, courses=courses)
        return '200 OK', [template.encode(encoding='utf-8')]

class CreateCourse:
    def __call__(self, request):
        page = 'create_course.html'
        categories = site.categories
        template = render(page, categories=categories)
        if request['method'] == 'POST':
            logger.log(f'Создали курс на основе полученных данных - {request["data"]}')
            data=request['data']
            new_course = site.create_course(type=data['type'], name=data['name'], category=data['category'])
            site.courses.append(new_course)
        return '200 OK', [template.encode(encoding='utf-8')]

class Categories:
    def __call__(self, request):
        page = 'categories.html'
        categories = site.categories
        template = render(page, categories=categories)
        if request['method'] == "POST":
            print(request['data'])
            new_cat = site.create_category(request['data']['name'])
            site.categories.append(new_cat)
        return '200 OK', [template.encode(encoding='utf-8')]