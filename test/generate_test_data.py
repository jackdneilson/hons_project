import glob
import subprocess


def generate_data(root_dir):
    for location in glob.glob(root_dir + '/lfw/**/*.jpg', recursive=True):
        file = open(location[:-3] + 'json', 'w')
        towrite = '{"name":"%s", "image_location":"%s"}' % (location.split('/')[-2], 'http://localhost:8081/static'+location[1:])
        file.write(towrite)
        file.close()

    for location in glob.glob(root_dir + '/lfw/**/*.png', recursive=True):
        file = open(location[:-4] + '_png.json', 'w')
        towrite = '{"name":"%s", "image_location":"%s"}' % (location.split('/')[-2], 'http://localhost:8081/static'+location[1:])
        file.write(towrite)
        file.close()

    for location in glob.glob(root_dir + '/essex_cswww/**/*.jpg', recursive=True):
        file = open(location[:-3] + 'json', 'w')
        towrite = '{"name":"%s", "image_location":"%s"}' % (location.split('/')[-2], 'http://localhost:8081/static'+location[1:])
        file.write(towrite)
        file.close()

    for location in glob.glob(root_dir + '/lfw/**/*.jpg', recursive=True):
        subprocess.run(["convert", location, location[:-3] + "png"])


generate_data('.')
