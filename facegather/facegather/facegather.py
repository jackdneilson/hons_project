from scipy import misc
from io import BytesIO
import requests
import face_recognition as fr

class Facegather:
    IMAGE_LOAD_MAX = 20

    @staticmethod
    def load_image(uri, remote = True):
        if (remote):
            resp = requests.get(uri)
            img_array = misc.imread(BytesIO(resp.content))
            return img_array
        else:
            img = fr.load_image_file(uri)
            return fr.face_encodings(img)
