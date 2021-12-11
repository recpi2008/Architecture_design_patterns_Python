from datetime import date
from views import Index, Contact


def secret_front(request):
    request['date'] = date.today()


def other_front(request):
    request['key'] = 'key'

def content_list(request):
    request['products_list'] = {'Автопортрет':"https://muzei-mira.com/templates/museum/images/paint/avtoportret-pablo-pikasso+.jpg",
                                'Внучка':''"https://m.buro247.ru/images/culture/f3c6069181eed025ac50b2d0ce101d6e.jpg",
                                'Париж':"https://static.kulturologia.ru/files/u18046/picasso-young-05.jpg",
                                'Любовница':"https://cdn.gallerix.asia/x/src/news/2012/345159912.jpg"}

fronts = [secret_front, other_front, content_list]

routes = {
    '/': Index(),
    '/contact/': Contact(),
}
