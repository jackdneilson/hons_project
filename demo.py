from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import json


class Handler(FileSystemEventHandler):
    def __init__(self):
        super()
        self.path = './demo'
        self.base_uri = 'http://localhost:8081/'

    def on_created(self, event):
        result_file = open(event.src_path, 'r')
        result_array = json.load(result_file)

        html_demo = open(self.path + '/demo.html', 'w')
        html_demo.write(
            '<!DOCTYPE html>'
            '<html lang="en">'
            '<head>'
            '<meta charset="UTF-8">'
            '<title>Facegather Demo</title>'
            ''
            '<link rel="stylesheet" type="text/css" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">'
            '</head>'
            ''
            '<body>'
            '<table class=".table .table-hover" style="width: 80%;">'
            '<tr>'
            '<th>Name</th>'
            '<th>Distance</th>'
            '<th>Image</th>'
            '</tr>'
        )

        for result in result_array:
            html_demo.write(
                '<tr>'
                '<td>' + result['name'] + '</td>'
                '<td>' + str(result['distance']) + '</td>'
                '<td><img src="' + self.base_uri + result['image_location'] + '"></td>'
                '</tr>'
            )

        html_demo.write('</table>')




path = './demo'
handler = Handler()

observer = Observer()
observer.schedule(handler, path)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()

