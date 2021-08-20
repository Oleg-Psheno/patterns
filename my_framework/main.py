def not_found_view(request):
    return '404 PAGE NOT FOUND', [b'Page not found...']


class Application:
    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        # Add '/' if not exists
        if path[-1] != '/':
            path = f'{path}/'
        if path in self.routes:
            view = self.routes[path]
        else:
            view = not_found_view
        request = {}
        for front in self.fronts:
            front(request)
        print(request)
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return body
