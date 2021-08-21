from my_framework.requests import PostRequests, GetRequests


def not_found_view(request):
    return '404 PAGE NOT FOUND', [b'Page not found...']


class Application:
    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        method = environ['REQUEST_METHOD']
        request = {}
        request['method'] = method
        if method == 'POST':
            request['data'] = PostRequests().get_params(environ)
        elif method == "GET":
            request['data'] = GetRequests().get_params(environ)

        print(method)
        # Add '/' if not exists
        if path[-1] != '/':
            path = f'{path}/'
        if path in self.routes:
            view = self.routes[path]
        else:
            view = not_found_view
        for front in self.fronts:
            front(request)
        print(request)
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return body
