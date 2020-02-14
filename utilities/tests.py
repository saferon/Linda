# TO DO: 1. Get more faces in KNOWN to compare to improve accuracy
#        2.Write Encodings to file?

# possibly: import face_recognition
#           image = face_recognition.load_image_file("my_picture.jpg")
#           face_locations = face_recognition.face_locations(image, model="cnn")
#           face_locations is now an array listing the co-ordinates of each face


import os
import face_recognition as facerec
import pickle
import shutil
import numpy as np
from multiprocessing.dummy import Pool

path = '/home/saferon/Documents/fixfix/pics/' # set to your path of unknown pictures
Unknown_array = os.listdir(path)
filesPath = '/home/saferon/Documents/fixfix/' # set to path containing the folders

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


# TO DO: 1. Get more faces in KNOWN to compare to improve accuracy
#        2.Write Encodings to file?

# possibly: import face_recognition
#           image = face_recognition.load_image_file("my_picture.jpg")
#           face_locations = face_recognition.face_locations(image, model="cnn")
#           face_locations is now an array listing the co-ordinates of each face


# import os
# import face_recognition as facerec
# import pickle
# import shutil
#
# path = '/home/saferon/Documents/fixfix/pics/'  # set to your path of unknown pictures
# Unknown_array = os.listdir(path)
# knownPath = '/home/saferon/Documents/fixfix/known/'  # set to your path of known images, name these files to the name of the person in the image, eg donaldtrump.jpg
# Known_array = os.listdir(knownPath)
# filesPath = '/home/saferon/Documents/fixfix/'  # set to path containing the folders
#
# Encoding_known = {}
#
# # dict holds all of encoding data with filename as key
# for known in Known_array:
#     # print(knownPath+known)
#     faceName = facerec.load_image_file(knownPath+known)
#     Encoding_known[known] = facerec.face_encodings(faceName)
#     # print(Encoding_known[known])
#
# for unknown in Unknown_array:
#     print("checking unknown: " + unknown)
#     faceName = facerec.load_image_file(path+unknown)
#     faceData = facerec.face_encodings(faceName)
#     if not faceData:
#         print("No face no case.")
#         print("--------------------------------------------")
#         continue
#     lowestFace = 100
#     lowestLinda = ""
#
#     for known in Encoding_known:
#         distance = facerec.face_distance(Encoding_known[known][0], faceData)
#         if len(distance) > 1:
#             print("More than one mug.")
#             continue
#         if distance < lowestFace:
#             lowestLinda = known
#             lowestFace = distance
#
#     finalLindaName = lowestLinda.split('.', 1)[0]
#     print("RARE " + finalLindaName.upper() + " DETECTED")
#
#     print("distance is: " + str(lowestFace))
#     print("should we move that shid? " + str(lowestFace < 0.6))
#
#     if lowestFace < 0.6:
#         if not os.path.exists(filesPath+finalLindaName):
#             os.makedirs(filesPath+finalLindaName)
#
#         shutil.move(path+unknown, filesPath+finalLindaName)
#     else:
#         print("shit match")
#
#     print("--------------------------------------------")


# path = '/home/saferon/Documents/fixfix/pics/' # set to your path of unknown pictures
# Unknown_array = os.listdir(path)
# knownPath = '/home/saferon/Documents/fixfix/known/' # set to your path of known images, name these files to the name of the person in the image, eg donaldtrump.jpg
# Known_array = os.listdir(knownPath)
# class Linda:
#     """holding all of the linda encodings, hopefully"""

#     def __init__(self, linda, path_to_linda, encoding):
#         self.name = linda
#         self.file_path = path_to_linda
#         self.encoding = encoding

# pickle_out = ("lindapickle", "wb")
# pickle.dump(var, pickle_out)
# pickle_out.close()
# pickle_in = open("lindapickle", "rb")




# # for x in range(0, len(Unknown_array)): # creates a list of arrays of the face_encodings to be read of the unknown faces
# #     unknownface = facerec.load_image_file(path+Unknown_array[x])
# #     EncodingFiles = Encoding_unknown.append(facerec.face_encodings(unknownface))

# for img in Unknown_array:
#     unknownface = facerec.load_image_file(path + img)
#     EncodingFiles = Encoding_unknown.append(facerec.face_encodings(unknownface))

# EucList = []

# for x in range(0, len(Encoding_unknown)):
#     euclistUnknown = Encoding_unknown[x][0]
#     euclistvar1 = facerec.face_distance(euclistUnknown, boEncode)
#     euclistvar2 = facerec.face_distance(euclistUnknown, luEncode)
#     euclistvar3 = facerec.face_distance(euclistUnknown, euEncode)
#     List = []
#     List.append(euclistvar1)
#     List.append(euclistvar2)
#     List.append(euclistvar3)
#     EucList.append(List)

# for x in range(0, len(Unknown_array)):
#     smallestED = min(EucList[x])
#     print(smallestED)

# # faces = { Known_array[x] : Encoding_known[x] for x in range(0, len(Known_array))}

# # List of strings
# # listOfStr = ["hello", "at" , "test" , "this" , "here" , "now" ]
# # dictOfWords = { i : listOfStr[i] for i in range(0, len(listOfStr) ) }
# # print(dictOfWords)

# # # for filenames in Known_array:

# # for x in Known_array:
# #     prevVar = Known_array[x]
# #     knownEncodingVar = facerec.face_encodings(prevVar)
