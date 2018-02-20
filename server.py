import cherrypy as cp
from subprocess import check_output


class EnumerateFiles(object):
    @cp.expose
    def index(self):
        return check_output("tree -J ./test", shell=True)


if __name__ == '__main__':
    cp.config.update({
        'server.socket_port': 8080,
        'tools.proxy.on': True,
        'tools.proxy.base': 'localhost'
    })
    cp.quickstart(EnumerateFiles())
