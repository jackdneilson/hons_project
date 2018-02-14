import cherrypy as cp
import os

class EnumerateFiles(object):
    @cp.expose
    def index(self):
        for root, dirs, files in os.walk('/home/jack/Documents/hons_project/test'):
            print(root)
            print(dirs)
        # TODO: Enumerate filesystem as a JSON object
        return os.stat(os.getcwd())


if __name__ == '__main__':
    cp.config.update({
        'server.socket_port': 8080,
        'tools.proxy.on': True,
        'tools.proxy.base': 'localhost'
    })
    cp.quickstart(EnumerateFiles())
