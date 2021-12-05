from simba_framework.templator import render


class Index:
    def __call__(self, request):
        return '200 OK', render('2.html', data=request.get('data', None))


class About:
    def __call__(self, request):
        return '200 OK', 'about'


class NotFound404:
    def __call__(self, request):
        return '404 WHAT', '404 PAGE Not Found'
