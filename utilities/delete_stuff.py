import os, glob
from multiprocessing.dummy import Pool
import shutil

pathy = "/home/saferon/Documents/for_linda/allknown/"

paths = []

for directory in os.listdir(pathy):
    paths.append(pathy + directory + '/')
    print("Appeded " + pathy + directory + " to paths list.")


def remove_bad_files(path):
    for files in os.listdir(path):
        if files.startswith("._") or os.stat(path + files).st_size == 0:
            shutil.move(path + files, '/home/saferon/Documents/for_linda/bad/')


for i in paths:
    remove_bad_files(i)
