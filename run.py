from facegather import facegather
import face_recognition

import os
# TODO: Implement args, server
# Get image to test from local filesystem
test_face = facegather.load_image(os.getcwd() + '/test/lfw/Aaron_Peirsol/Aaron_Peirsol_0001.jpg', remote=False)
test_face2 = facegather.load_image(os.getcwd() + '/test/lfw/Aaron_Peirsol/Aaron_Peirsol_0002.jpg', remote=False)
result = face_recognition.face_distance([test_face], test_face2)
print(result)
# results = someshit.search(test_face, '192.168.0.1', no_threads=4)
