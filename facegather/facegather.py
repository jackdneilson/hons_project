from scipy import misc
from io import BytesIO
import requests
import face_recognition as fr
import threading
import queue
import collections

IMAGE_LOAD_MAX = 20
img_uri_queue = queue.Queue()
img_uri_queue_lock = threading.Lock()
img_queue = queue.Queue()
img_queue_lock = threading.Lock()


# Load an image in to memory from local or remote sources
def load_image(uri, remote=True):
    if remote:
        resp = requests.get(uri)
        img_array = misc.imread(BytesIO(resp.content))
        return img_array
    else:
        img = fr.load_image_file(uri)
    return fr.face_encodings(img)[0]


def search(test_face, uri, no_threads=1, max_loaded=IMAGE_LOAD_MAX):
    result = collections.deque(maxlen=5)
    img_uri_queue_counter = threading.Semaphore(max_loaded)

    print('Getting profile information...', end='', flush=True)
    profiles = _get_profiles(uri)
    # TODO: Parse profiles to fill queue
    for profile in profiles:
        img_uri_queue.put([profile.img_link, profile.link])
    print('Done')

    print('Processing images...', end='', flush=True)
    for i in range(0, no_threads):
        thread = ImageProcessor(img_uri_queue_counter)
        thread.start()

    recogniser = FaceRecogniser(test_face, img_uri_queue_counter, result)
    recogniser.start()
    recogniser.join()
    print('Done')

    # TODO: Return result
    return None


# TODO: Use more identifying information
def _get_profiles(uri, name=None, dob=None):
    resp = requests.get(uri)
    return resp.json()


# Class based thread to take an image URI from the queue, download it, and preprocess it to be ready for facial
# recognition by 1 or more FaceRecogniser threads
class ImageProcessor(threading.Thread):
    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

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

            img = load_image(img_uri[0])
            img_queue_lock.acquire()
            img_queue.put([img, img_uri[1]])
            img_queue_lock.release()


# Class based thread to take images loaded in to memory and rank them in terms of similarity to the test image.
class FaceRecogniser(threading.Thread):
    finished_flag = False

    def __init__(self, test_face, counter, result):
        threading.Thread.__init__(self)
        self.test_face = test_face
        self.counter = counter
        self.result = result

    def run(self):
        while not img_queue.empty() or not FaceRecogniser.finished_flag:
            img_queue_lock.acquire()
            self.counter.release()
            img = img_queue.get()
            img_queue_lock.release()

            # TODO: Write logic for recognising and ranking (remember list)
            similarity = fr.compare_faces([self.test_face], img[0])
            self.result.insert()