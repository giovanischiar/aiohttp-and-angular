import asyncio
from aiohttp import web

class HttpServer():
    def run(self):
        app = web.Application()
        app.router.add_route(
            'GET',
            '/route',
            self.route_handler)
        app.router.add_static('/', '../cliente');
        handler = app.make_handler()
        loop = asyncio.get_event_loop()
        server = loop.create_server(
            handler,
            '127.0.0.1',
            8080)
        srv = loop.run_until_complete(server)
        print("servidor rodando!");
        return srv

    @asyncio.coroutine
    def route_handler(self, request):
        print('cliente enviou uma requisição')
        return web.Response(text='funcionou!');