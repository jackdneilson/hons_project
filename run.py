from facegather import facegather
import face_recognition
import os
import argparse


# TODO: Implement server
def main():
    parser = argparse.ArgumentParser
    parser.add_argument("test_face")
    parser.add_argument("service")

    parser.add_argument("--pthreads")
    parser.add_argument("--cthreads")
    parser.add_argument("--maxload")

    args = parser.parse_args()

    # TODO: Generate URI from service name
    result = facegather.search(args.test_face, args.service, args.pthreads, args.cthreads, args.maxload)

    test_face = facegather.load_images(os.getcwd() + '/test/lfw/Aaron_Peirsol/Aaron_Peirsol_0001.jpg', remote=False)[0]
    test_face2 = facegather.load_images(os.getcwd() + '/test/lfw/Aaron_Peirsol/Aaron_Peirsol_0002.jpg', remote=False)[0]
    result = face_recognition.face_distance([test_face], test_face2)
    print(result)
    # results = someshit.search(test_face, , no_threads=4)
    # def search(test_face, uri, no_producer_threads=1, no_consumer_threads=1, max_loaded=IMAGE_LOAD_MAX):


