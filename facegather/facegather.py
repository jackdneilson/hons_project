from PIL import Image
import requests
import face_recognition as fr
import threading
import queue
import numpy
import sortedcontainers

IMAGE_LOAD_MAX = 200
DEFAULT_THRESHOLD = 0.5
profile_queue = queue.Queue()
img_queue = queue.Queue()


# Load an image in to memory from local or remote sources
def load_images(uri, remote=True):
    if remote:
        print('Retrieving image from ' + uri)
        resp = requests.get(uri, stream=True)
        resp.raw.decode_content = True
        img = Image.open(resp.raw)
        return fr.face_encodings(numpy.array(img))
    else:
        print('Retrieving image from ' + uri)
        img_array = fr.load_image_file(uri)
    return fr.face_encodings(img_array)


# Search a data set at the given URI for the best matches to the test face
def search(test_face_location,
           uri,
           no_producer_threads=None,
           no_consumer_threads=None,
           max_loaded=None,
           threshold=None,
           name=None):
    # Load default values in case called with "None"
    if no_producer_threads is None:
        no_producer_threads = 1
    if no_consumer_threads is None:
        no_consumer_threads = 1
    if max_loaded is None:
        max_loaded = IMAGE_LOAD_MAX
    if threshold is None:
        threshold = DEFAULT_THRESHOLD

    result = sortedcontainers.SortedListWithKey(key=lambda val: val[0])
    result_lock = threading.Lock()

    profile_queue_counter = threading.Semaphore(max_loaded)
    print('Getting profile information...')
    profiles = ''
    if name is None:
        profiles = _get_profiles(uri)
    else:
        profiles = _get_profiles(uri + '/?name=' + name)
    for profile in profiles:
        profile_queue.put([uri + '/' + profile['image_location'], profile])
        print('Loaded ' + profile['name'])
    print('Done')

    print('Processing images...')
    for i in range(0, int(no_producer_threads)):
        processor = ImageProcessor(profile_queue_counter)
        processor.start()

    recogniser_list = []
    for i in range(0, int(no_consumer_threads)):
        recogniser = FaceRecogniser(test_face_location, profile_queue_counter, result, result_lock, threshold)
        recogniser.start()
        recogniser_list.append(recogniser)

    for recogniser in recogniser_list:
        recogniser.join()

    print('Done')
    return result


# TODO: Use more identifying information
def _get_profiles(uri, name=None):
    if name is not None:
        uri += '?name='
        uri += name
    resp = requests.get(uri)
    return resp.json()


# Class based thread to take a profile from the queue, download the profile photo, and pre-process it to be ready for
# facial recognition by 1 or more FaceRecogniser threads
class ImageProcessor(threading.Thread):
    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.waiting_counter = counter

    # Take a URI from the queue, download image from that location then add face mappings and profile uri to the queue
    # to be consumed by a FaceRecogniser
    def run(self):
        while True:
            self.waiting_counter.acquire()
            if profile_queue.empty():
                sentinel = Sentinel()
                img_queue.put(sentinel)
                return
            profile = profile_queue.get()

            img_array = load_images(profile[0])
            for img in img_array:
                img_queue.put([img, profile[1]])


# Class based thread to take images loaded in to memory and rank them in terms of similarity to the test image.
class FaceRecogniser(threading.Thread):
    finished_flag = False

    def __init__(self, test_face_location, waiting_counter, result, result_lock, threshold):
        threading.Thread.__init__(self)
        self.test_face = fr.face_encodings(fr.load_image_file(test_face_location))[0]
        self.counter = waiting_counter
        self.result = result
        self.result_lock = result_lock
        self.threshold = threshold

    # Take a face mapping from the queue, then test for similarity.
    def run(self):
        while True:
            self.counter.release()
            img = img_queue.get()
            if img is Sentinel:
                return

            # if fr.face_distance([self.test_face], img[0]) < self.result[-1][0]:
            #    distance = fr.face_distance([self.test_face], img[0])
            #    print(distance)
            #    self.result.add([distance, img[1]])
            #    self.result.pop()
            if fr.face_distance([self.test_face], img[0] < self.threshold):
                distance = fr.face_distance([self.test_face], img[0])
                self.result_lock.acquire()
                self.result.add([distance, img[1]])
                self.result_lock.release()


class Sentinel:
    def __init__(self):
        super()
