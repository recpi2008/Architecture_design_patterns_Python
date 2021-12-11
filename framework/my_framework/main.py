from quopri import decodestring
from requests import GetRequests, PostRequests



class PageNotFound404:
    def __call__(self, request):
        return '404 status', '404 PAGE Not Found'


class Myframework:

    """Myframework basis framework"""

    def __init__(self, routes, fronts):
        self.routes_list = routes
        self.fronts_list = fronts

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']

        if not path.endswith('/'):
            path = f'{path}/'

        request = {}
        method = environ['REQUEST_METHOD']
        request['method'] = method

        if method == 'POST':
            data = PostRequests().get_request_params(environ)
            request['data'] = data
            print(f'Post запрос: {Myframework.decode_value(data)}')
        if method == 'GET':
            gets_params = GetRequests().get_request_params(environ)
            request['gets_params'] = gets_params
            print(f'Параметры GET: {gets_params}')


        if path in self.routes_list:
            view = self.routes_list[path]
        else:
            view = PageNotFound404()


        for front in self.fronts_list:
            front(request)
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]

    @staticmethod
    def decode_value(data):
        new_data = {}
        for k, v in data.items():
            val = bytes(v.replace('%', '=').replace("+", " "), 'UTF-8')
            val_decode_str = decodestring(val).decode('UTF-8')
            new_data[k] = val_decode_str
        return new_data
