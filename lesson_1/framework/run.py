from wsgiref.simple_server import make_server

from my_framework.main import Myframework
from urls import routes, fronts


application = Myframework(routes, fronts)

with make_server('', 8000, application) as httpd:
    print("Запуск Myframework...")
    httpd.serve_forever()