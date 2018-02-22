import cherrypy as cp
import glob


class EnumerateFiles(object):
    @cp.expose
    def index(self, **kwargs):
        directory = 'test/**'
        if 'name' in kwargs:
            directory = 'test/lfw/' + kwargs['name']

        sb = '['
        for location in glob.glob(directory + '/*.json', recursive=True):
            f = open(location, 'r')
            sb += f.read()
            sb += ','
            f.close()
        if sb.endswith('['):
            return '[]'
        else:
            return sb[:-1] + ']'


if __name__ == '__main__':
    cp.config.update({
        'server.socket_port': 8080,
        'tools.proxy.on': True,
        'tools.proxy.base': 'localhost'
    })
    cp.quickstart(EnumerateFiles())
