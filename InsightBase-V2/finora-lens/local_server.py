"""Offline, loopback-only server for the adjacent dashboard and dataa.xlsx."""
import argparse
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit, unquote
import webbrowser

ALLOWED = {'index.html', 'styles.css', 'app.js', 'structure.js', 'engine.js', 'xlsx.js', 'dataa.xlsx'}

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        path = unquote(urlsplit(self.path).path)
        filename = 'index.html' if path == '/' else path.lstrip('/')
        if filename not in ALLOWED or path.count('/') > 1:
            self.send_error(404)
            return
        super().do_GET()

    def do_HEAD(self):
        path = unquote(urlsplit(self.path).path)
        filename = 'index.html' if path == '/' else path.lstrip('/')
        if filename not in ALLOWED or path.count('/') > 1:
            self.send_error(404)
            return
        super().do_HEAD()

    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('Cross-Origin-Resource-Policy', 'same-origin')
        super().end_headers()

    def log_message(self, *args):
        pass

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=8765)
    parser.add_argument('--no-browser', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    factory = lambda *a, **kw: Handler(*a, directory=str(root), **kw)
    try:
        server = ThreadingHTTPServer(('127.0.0.1', args.port), factory)
    except OSError:
        server = ThreadingHTTPServer(('127.0.0.1', 0), factory)
    url = f'http://127.0.0.1:{server.server_port}/'
    print(f'Sektovista: {url}\ndataa.xlsx is read from: {root}\nKeep this window open. Close it to stop.', flush=True)
    if not args.no_browser:
        webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()

if __name__ == '__main__':
    main()
