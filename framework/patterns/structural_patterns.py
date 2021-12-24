from time import time


class AppRoute:
    def __init__(self, routes, url):
        self.routes = routes
        self.url = url

    def __call__(self, cls):
        self.routes[self.url] = cls()


class Debug:

    def __init__(self, name):
        self.name = name

    def __call__(self, cls):
        def timeit(method):
            def timed(*args, **kw):
                tfirst = time()
                result = method(*args, **kw)
                tend = time()
                delta = tend - tfirst

                print(f'Debug {self.name} выполнялся за {delta:2.2f} ms')
                return result

            return timed

        return timeit(cls)
