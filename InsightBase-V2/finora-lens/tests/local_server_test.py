import importlib.util, tempfile, threading, unittest
from pathlib import Path
from http.server import ThreadingHTTPServer
from urllib.request import urlopen
from urllib.error import HTTPError

spec=importlib.util.spec_from_file_location('server',Path(__file__).parents[1]/'local_server.py')
server=importlib.util.module_from_spec(spec)
spec.loader.exec_module(server)

class LocalServerTest(unittest.TestCase):
    def test_local_file_contract(self):
        with tempfile.TemporaryDirectory() as d:
            folder=Path(d)
            (folder/'index.html').write_text('<h1>Test</h1>')
            (folder/'private.txt').write_text('not served')
            factory=lambda *a,**kw: server.Handler(*a,directory=d,**kw)
            http=ThreadingHTTPServer(('127.0.0.1',0),factory)
            thread=threading.Thread(target=http.serve_forever,daemon=True)
            thread.start()
            base='http://127.0.0.1:'+str(http.server_port)
            try:
                with urlopen(base+'/') as r:
                    self.assertIn(b'Test',r.read())
                for path in ['/dataa.xlsx','/private.txt','/../private.txt']:
                    with self.assertRaises(HTTPError) as error:
                        urlopen(base+path)
                    self.assertEqual(error.exception.code,404)
                (folder/'dataa.xlsx').write_bytes(b'first workbook')
                with urlopen(base+'/dataa.xlsx') as r:
                    self.assertEqual(r.read(),b'first workbook')
                    self.assertEqual(r.headers['Cache-Control'],'no-store')
                (folder/'dataa.xlsx').write_bytes(b'updated workbook')
                with urlopen(base+'/dataa.xlsx') as r:
                    self.assertEqual(r.read(),b'updated workbook')
            finally:
                http.shutdown();http.server_close();thread.join()

if __name__=='__main__':
    unittest.main()
