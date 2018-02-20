from facegather import facegather
import face_recognition
import argparse


parser = argparse.ArgumentParser(
    description='A python3 program to gather social media intelligence using facial recognition')
parser.add_argument("test_face", help='Location of the test face')
parser.add_argument("service", help='Social network service to search')

parser.add_argument("--pthreads", help='Number of image processing threads')
parser.add_argument("--cthreads", help='Number of image comparison threads')
parser.add_argument("--maxload", help='Maximum number of images pre-loaded into memory')

args = parser.parse_args()

uri = ''
if args.service == 'demo':
    uri = 'http://localhost:8081/static'

    test_face = facegather.load_images(uri + '/lfw/Aaron_Peirsol/Aaron_Peirsol_0001.jpg')[0]
    test_face2 = facegather.load_images(uri + '/lfw/Aaron_Peirsol/Aaron_Peirsol_0002.jpg')[0]
    result = face_recognition.face_distance([test_face], test_face2)
    print(result)

    test_face = facegather.load_images(
        '/home/jack/Documents/hons_project/test/lfw/Aaron_Peirsol/Aaron_Peirsol_0001.jpg',
        remote=False)[0]
    test_face2 = facegather.load_images(
        '/home/jack/Documents/hons_project/test/lfw/Aaron_Peirsol/Aaron_Peirsol_0002.jpg',
        remote=False)[0]
    result = face_recognition.face_distance([test_face], test_face2)
    print(result)

elif args.service == 'test':
    uri = 'http://localhost:8081'
    result = facegather.search(args.test_face, uri, args.pthreads, args.cthreads, args.maxload)
    print(result)
# result = facegather.search(args.test_face, uri, args.pthreads, args.cthreads, args.maxload)
