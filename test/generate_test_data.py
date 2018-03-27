import glob
import os

os.sep = '/'

def generate_data(root_dir):
    print(glob.glob(root_dir + '/lfw/**/*.jpg', recursive=True))
    for location in glob.glob(root_dir + '/lfw/**/*.jpg', recursive=True):
        file = open(location[:-3] + 'json', 'w')
        towrite = '{"name":"%s", "image_location":"%s"}' % (location.split('/')[-2], 'static'+location[1:])
        file.write(towrite)
        file.close()

    for location in glob.glob(root_dir + '/essex_cswww/**/*.jpg', recursive=True):
        file = open(location[:-3] + 'json', 'w')
        towrite = '{"name":"%s", "image_location":"%s"}' % (location.split('/')[-2], 'static'+location[1:])
        file.write(towrite)
        file.close()


generate_data('.')
