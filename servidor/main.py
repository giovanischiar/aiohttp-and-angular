import asyncio
from servidor import HttpServer

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    srv = HttpServer().run()
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        loop.run_until_complete(handler.finish_connections(1.0))
        srv.close()
        loop.run_until_complete(srv.wait_closed())
        loop.run_until_complete(app.finish())
    loop.close()