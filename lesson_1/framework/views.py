from my_framework.templator import render



class Index:
    def __call__(self, request):
        print(request)
        return '200 OK', render('index.html', data=request)


class Contact:
    def __call__(self, request):
        return '200 OK', render('contact.html', data=request)


class NotFound404:
    def __call__(self, request):
        return '404 WHAT', '404 PAGE Not Found'
