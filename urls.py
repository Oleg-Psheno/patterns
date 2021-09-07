from views import index_view, about_view, Other, Contacts, CourseList, CreateCourse, Categories

routes = {
    '/': index_view,
    '/about/': about_view,
    '/other/': Other(),
    '/contacts/': Contacts(),
    '/courses/': CourseList(),
    '/create-course/': CreateCourse(),
    '/categories/': Categories(),
}

def first_front(request):
    request['first'] = 'first front'

def second_front(request):
    request['second'] = 'second front'

fronts = [first_front, second_front]