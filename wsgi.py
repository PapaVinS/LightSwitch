# from gevent.pywsgi import WSGIServer
# from server import app

# http_server = WSGIServer(('', 5000), app)
# http_server.serve_forever()from server import backend

if __name__ == "__main__":
    backend.run()
