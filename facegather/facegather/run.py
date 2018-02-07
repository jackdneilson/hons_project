import face_recognition as fr
from .facegather import Facegather

# TODO: Implement args
# Get image to test from local filesystem
test_face = Facegather.load_image('test.jpg', remote = False)

# TODO: Function to load in a producer thread, using facegather.max. Use encodings. Store links in dict.
dataset = Facegather.load_image('192.168.0.1')

# TODO: Multiple consumer threads to check against test image, single output list of size 5 with results (in dict
# TODO: to get at original link)
results = fr.compare_faces(test_face, dataset)
