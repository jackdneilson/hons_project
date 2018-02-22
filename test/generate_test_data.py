import glob


def generate_data(root_dir):
    for location in glob.glob(root_dir + '/**/*.jpg', recursive=True):
        file = open(location[:-3] + 'json', 'w')
        towrite = '{"name":"%s", "image_location":"%s"}' % (location.split('/')[-2], 'static'+location[1:])
        file.write(towrite)
        file.close()


generate_data('.')
