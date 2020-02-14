# TO DO: 1. Get more faces in KNOWN to compare to improve accuracy
#        2.Write Encodings to file?

import threading
import shutil
import os
import face_recognition as facerec
import numpy as np
try:
    import cPickle as pickle
except:
    import pickle
from multiprocessing.dummy import Pool
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

filesPath = '/home/saferon/Documents/for_linda/allknown/'  # set to path containing the folders

Encoding_known = {}
names_and_codes = []


paths = []

for directory in os.listdir(filesPath):
    paths.append(filesPath + directory + '/')
    print("Appeded " + filesPath + directory + " to paths list.")

names_and_codes = []


def pickler(path):
    for images in os.listdir(path):
        if ".webm" not in images and ".mp4" not in images and ".gif" not in images and ".ini" not in images:
            print(images)
            names_and_codes.append((
                path,
                facerec.face_encodings(
                    facerec.load_image_file(path + images)
                )
            ))
            print("Appended " + images + " to names_and_codes list.")
            print(len(names_and_codes))


pool = Pool()
pool.map(pickler, paths)
pool.close()
pool.join()
# slow method without multithreading
# for pathz in paths:
#     pickler(pathz)

pickle.dump(names_and_codes, open('archive', 'wb'))
print("All encodings dumped to pickle!")
