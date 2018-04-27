import glob


def generate_data(root_dir):
    for location in glob.glob(root_dir + '/lfw/**/*.jpg', recursive=True):
        file = open(location[:-3] + 'json', 'w')
        towrite = '{"name":"%s", "image_location":"%s"}' % (location.split('/')[-2], 'http://localhost:8081/static'+location[1:])
        file.write(towrite)
        file.close()

    # for location in glob.glob(root_dir + '/lfw/**/*.jpg', recursive=True):
    #    print(location)
    #    subprocess.run(["convert", location, "-colorspace", "sRGB", "-type", "truecolor", location[:-3] + "png"])

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

    # SCface db has several formats, need to be specific
    for location in glob.glob(root_dir + '/SCface/SCface_database/mugshot_frontal_cropped_all/*.JPG', recursive=True):
        file = open(location[:-12] + '.json', 'w')
        towrite = '{"name":"%s", "image_location":"%s"}' % (location.split('/')[-1][:3], 'http://localhost:8081/static'+location[1:])
        file.write(towrite)
        file.close()

    for location in glob.glob(root_dir + '/SCface/SCface_database/mugshot_frontal_original_all/*.jpg', recursive=True):
        file = open(location[:-12] + '.json', 'w')
        towrite = '{"name":"%s", "image_location":"%s"}' % (location.split('/')[-1][:3], 'http://localhost:8081/static'+location[1:])
        file.write(towrite)
        file.close()

    for location in glob.glob(root_dir + '/SCface/SCface_database/mugshot_rotation_all/*.jpg', recursive=True):
        name = location.split('/')[-1][:-4]
        towrite = '{"name":"%s", "image_location":"%s"}' % (name, 'http://localhost:8081/static' + location[1:])
        file = open(location[:-3] + 'json', 'w')
        file.write(towrite)
        file.close()

    for location in glob.glob(root_dir + '/SCface/SCface_database/surveillance_cameras_*/**/*.jpg', recursive=True):
        name = location.split('/')[-1][:-4]
        towrite = '{"name":"%s", "image_location":"%s"}' % (name, 'http://localhost:8081/static' + location[1:])
        file = open(location[:-3] + 'json', 'w')
        file.write(towrite)
        file.close()


generate_data('.')
