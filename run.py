from my_framework.main import Application
from wsgiref.simple_server import make_server
from urls import routes, fronts


if __name__ == '__main__':
    application = Application(routes, fronts)

    with make_server('', 8070, application) as httpd:
        print('Start server...')
        httpd.serve_forever()
