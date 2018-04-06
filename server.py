import cherrypy as cp
import glob


class EnumerateFiles:
    @cp.expose
    def index(self, **kwargs):
        directory = 'test/**'
        if 'name' in kwargs:
            directory = 'test/**/' + kwargs['name']

        sb = '['
        for location in glob.glob(directory + '/*.json', recursive=True):
            if location[-9:] is not '_png.json':
                f = open(location, 'r')
                sb += f.read()
                sb += ','
                f.close()
        if sb.endswith('['):
            return '[]'
        else:
            return sb[:-1] + ']'


class TestMultipleDB:
    @cp.expose
    def index(self, **kwargs):
        directories = ['test/lfw/', 'test/essex_cswww/']
        sb = '['
        for directory in directories:
            if 'name' in kwargs:
                directory = directory + kwargs['name'] + '/'
            for location in glob.glob(directory + '**/*.json', recursive=True):
                f = open(location, 'r')
                sb += f.read()
                sb += ','
                f.close()
        sb = sb[:-1] + ']'
        return sb


class TestImageCompression:
    @cp.expose
    def index(self):
        sb = '['
        for location in glob.glob('test/lfw/**/*_png.json', recursive=True):
            f = open(location, 'r')
            sb += f.read()
            sb += ','
            f.close()
        sb = sb[:-1] + ']'
        return sb


if __name__ == '__main__':
    cp.config.update({
        'server.socket_port': 8080,
        'tools.proxy.on': True,
        'tools.proxy.base': 'localhost'
    })

    home = EnumerateFiles()

    cp.tree.mount(EnumerateFiles(), '/', None)
    cp.tree.mount(TestMultipleDB(), '/test_multiple_datasets', None)
    cp.tree.mount(TestImageCompression(), '/test_image_compression', None)
    
    cp.engine.start()
    cp.engine.block()
