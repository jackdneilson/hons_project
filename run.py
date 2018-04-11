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
parser.add_argument("--name", help='Name of person of interest')
parser.add_argument("--output_location", help='Location of results file')

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
    uri = 'http://localhost:8081/'
    result = ''
    if args.name is not None:
        if args.output_location is not None:
            result = facegather.search(
                args.test_face,
                uri,
                no_producer_threads=args.pthreads,
                no_consumer_threads=args.cthreads,
                max_loaded=args.maxload,
                name=args.name,
                output_location=args.output_location
            )
        else:
            result = facegather.search(
                args.test_face,
                uri,
                no_producer_threads=args.pthreads,
                no_consumer_threads=args.cthreads,
                max_loaded=args.maxload,
                name=args.name
            )
    else:
        if args.output_location is not None:
            result = facegather.search(
                args.test_face,
                uri,
                no_producer_threads=args.pthreads,
                no_consumer_threads=args.cthreads,
                max_loaded=args.maxload,
                output_location=args.output_location
            )
        else:
            result = facegather.search(
                args.test_face,
                uri,
                no_producer_threads=args.pthreads,
                no_consumer_threads=args.cthreads,
                max_loaded=args.maxload,
            )
    print(result)

elif args.service == 'test_multiple_db':
    uri = 'http://localhost:8081/test_multiple_datasets/'
    result = ''
    if args.name is not None:
        if args.output_location is not None:
            result = facegather.search(
                args.test_face,
                uri,
                no_producer_threads=args.pthreads,
                no_consumer_threads=args.cthreads,
                max_loaded=args.maxload,
                name=args.name,
                output_location=args.output_location
            )
        else:
            result = facegather.search(
                args.test_face,
                uri,
                no_producer_threads=args.pthreads,
                no_consumer_threads=args.cthreads,
                max_loaded=args.maxload,
                name=args.name
            )
    else:
        if args.output_location is not None:
            result = facegather.search(
                args.test_face,
                uri,
                no_producer_threads=args.pthreads,
                no_consumer_threads=args.cthreads,
                max_loaded=args.maxload,
                output_location=args.output_location
            )
        else:
            result = facegather.search(
                args.test_face,
                uri,
                no_producer_threads=args.pthreads,
                no_consumer_threads=args.cthreads,
                max_loaded=args.maxload,
            )
    print(result)

elif args.service == 'test_image_compression':
    uri = 'http://localhost:8081/test_image_compression/'
    result = ''
    if args.name is not None:
        if args.output_location is not None:
            result = facegather.search(
                args.test_face,
                uri,
                no_producer_threads=args.pthreads,
                no_consumer_threads=args.cthreads,
                max_loaded=args.maxload,
                name=args.name,
                output_location=args.output_location
            )
        else:
            result = facegather.search(
                args.test_face,
                uri,
                no_producer_threads=args.pthreads,
                no_consumer_threads=args.cthreads,
                max_loaded=args.maxload,
                name=args.name
            )
    else:
        if args.output_location is not None:
            result = facegather.search(
                args.test_face,
                uri,
                no_producer_threads=args.pthreads,
                no_consumer_threads=args.cthreads,
                max_loaded=args.maxload,
                output_location=args.output_location
            )
        else:
            result = facegather.search(
                args.test_face,
                uri,
                no_producer_threads=args.pthreads,
                no_consumer_threads=args.cthreads,
                max_loaded=args.maxload,
            )
    print(result)
