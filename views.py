from my_framework.templator import render


def index_view(request):
    page = 'templates/template.html'
    template = render(page, param='Test param')
    return '200 OK', [template.encode(encoding='utf-8')]


def about_view(request):
    return '200 OK', [b'About']


def not_found_view(request):
    return '404 PNF', [b'Page not found...']


class Other:
    def __call__(self, request):
        return '200 OK', [b'Other']
