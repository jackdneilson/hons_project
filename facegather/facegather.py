from PIL import Image
import requests
import face_recognition as fr
import threading
import queue
import collections
import numpy

IMAGE_LOAD_MAX = 20
img_uri_queue = queue.Queue()
img_uri_queue_lock = threading.Lock()
img_queue = queue.Queue()
img_queue_lock = threading.Lock()


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
def search(test_face, uri, no_producer_threads=1, no_consumer_threads=1, max_loaded=IMAGE_LOAD_MAX):
    # Load default values in case called with "None"
    if no_producer_threads is None:
        no_producer_threads = 1
    if no_consumer_threads is None:
        no_consumer_threads = 1
    if max_loaded is None:
        max_loaded = IMAGE_LOAD_MAX

    result = collections.deque(maxlen=5)
    result.extend([-1, -1, -1, -1, -1])
    result_lock = threading.Lock()
    min_result_value = -1
    img_uri_queue_counter = threading.Semaphore(max_loaded)

    print('Getting profile information...', end='', flush=True)
    profiles = _get_profiles(uri)
    for profile in profiles:
        img_uri_queue.put([profile.img_link, profile])
    print('Done')

    print('Processing images...', end='', flush=True)
    for i in range(0, no_producer_threads):
        processor = ImageProcessor(img_uri_queue_counter)
        processor.start()

    recogniser_list = []
    for i in range(0, no_consumer_threads):
        recogniser = FaceRecogniser(test_face, img_uri_queue_counter, result, result_lock, min_result_value)
        recogniser.start()
        recogniser_list.append(recogniser)

    for recogniser in recogniser_list:
        recogniser.join()
    print('Done')

    # TODO: Return result
    return None


# TODO: Use more identifying information
def _get_profiles(uri, name=None, dob=None):
    resp = requests.get(uri)
    return resp.json()


# Class based thread to take an image URI from the queue, download it, and pre-process it to be ready for facial
# recognition by 1 or more FaceRecogniser threads
class ImageProcessor(threading.Thread):
    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    # Take a URI from the queue, download image from that location then add face mappings and profile uri to the queue
    # to be consumed by a FaceRecogniser
    def run(self):
        while True:
            img_uri_queue_lock.acquire()
            self.counter.acquire()
            if img_uri_queue.empty():
                FaceRecogniser.finished_flag = True
                img_uri_queue_lock.release()
                return
            img_uri = img_uri_queue.get()
            img_uri_queue_lock.release()

            img_array = load_images(img_uri[0])
            img_queue_lock.acquire()
            for img in img_array:
                img_queue.put([img, img_uri[1]])
            img_queue_lock.release()


# Class based thread to take images loaded in to memory and rank them in terms of similarity to the test image.
class FaceRecogniser(threading.Thread):
    finished_flag = False

    def __init__(self, test_face, counter, result, result_lock, min_result_value):
        threading.Thread.__init__(self)
        self.test_face = test_face
        self.counter = counter
        self.result = result
        self.result_lock = result_lock
        self.min_result_value = min_result_value

    # Take a face mapping from the queue, then test for similarity.
    def run(self):
        while not img_queue.empty() or not FaceRecogniser.finished_flag:
            img_queue_lock.acquire()
            self.counter.release()
            img = img_queue.get()
            img_queue_lock.release()

            self.result_lock.acquire()
            if fr.face_distance([self.test_face], img[0]) > self.min_result_value:
                distance = fr.face_distance([self.test_face], img[0])
                for pos, r in self.result:
                    if r[2] < distance:
                        self.result.pop()
                        self.result.insert(pos, [r[0], r[1], distance])
                self.min_result_value = self.result[4][2]
            self.result_lock.release()
