from pathlib import Path

from werkzeug.exceptions import NotFound
from werkzeug.middleware.shared_data import SharedDataMiddleware
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.wrappers import Request, Response

from api import create_app

frontend = SharedDataMiddleware(NotFound(), {
  '/js/': '../frontend/dist/js/',
  '/css/': '../frontend/dist/css/',
  '/img/': '../frontend/dist/img/',
  '/': '../frontend/dist/index.html'
})

app = DispatcherMiddleware(frontend, {'/api': create_app()})

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('127.0.0.1', 5000, app, use_debugger = True, use_reloader = True)
