# TO DO: 1. Get more faces in KNOWN to compare to improve accuracy
#        2.Write Encodings to file?

# possibly: import face_recognition
#           image = face_recognition.load_image_file("my_picture.jpg")
#           face_locations = face_recognition.face_locations(image, model="cnn")
#           face_locations is now an array listing the co-ordinates of each face


import os
import face_recognition as facerec
import shutil
import numpy as np
from multiprocessing.dummy import Pool
try:
    import cPickle as pickle
except:
    import pickle


path = '/home/saferon/Documents/fixfix/pics/'  # set to your path of unknown pictures
Unknown_array = os.listdir(path)
filesPath = '/home/saferon/Documents/fixfix/'  # set to path containing the folders

names_and_codes = pickle.load(open('archive', 'rb'))
print(names_and_codes)


def sort_images(directory):
    """Sort all the images in a directory."""
    for unknown in directory:
        if ".webm" not in unknown and ".mp4" not in unknown and ".gif" not in unknown and ".ini" not in unknown:
            print("checking unknown: " + unknown)
            faceName = facerec.load_image_file(path+unknown)
            faceData = facerec.face_encodings(faceName)
            if not faceData:
                print("No face no case.")
                print("--------------------------------------------")
                continue
            lowestFace = 100
            lowestLinda = ""

            for names in names_and_codes:
                print(str(names[0]) + str(unknown))
                try:
                    distance = facerec.face_distance(names[1][0], faceData)
                    if len(distance) > 1:
                        # print("More than one mug.")
                        continue
                    if distance < lowestFace:
                        lowestLinda = names[0]
                        lowestFace = distance
                except IndexError:
                    print("no encodings detected")
                    pass

            finalLindaName = lowestLinda.split('.', 1)[0]
            print("RARE " + finalLindaName.upper() + " DETECTED")

            print("distance is: " + str(lowestFace))
            print("should we move that shid? " + str(lowestFace < 0.6))

            if lowestFace < 0.6 and not os.path.exists(names[0]+unknown):
                shutil.move(path+unknown, finalLindaName)
            else:
                print("shit match")

            print("--------------------------------------------")


splite = int(len(Unknown_array))/8
unknown_split = np.array_split(Unknown_array, splite)
pool = Pool()
pool.map(sort_images, unknown_split)
pool.close()
pool.join()
