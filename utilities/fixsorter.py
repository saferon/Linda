import os
import shutil

path = "C:\\Users\\camer\\Desktop\\plsfixfix\\"
names = os.listdir(path)
folder_name = ['pics', 'webm']

for x in range(0, 2):
    if not os.path.exists(path+folder_name[x]):
        os.makedirs(path+folder_name[x])

for files in names:
    if ".png" in files and not os.path.exists(path+'pics\\'+files):
        shutil.move(path+files, path+'pics\\'+files)
    if ".jpg" in files and not os.path.exists(path+'pics\\'+files):
        shutil.move(path+files, path+'pics\\'+files)
    if ".jpeg" in files and not os.path.exists(path+'pics\\'+files):
        shutil.move(path+files, path+'pics\\'+files)
    if ".webm" in files and not os.path.exists(path+'webm\\'+files):
        shutil.move(path+files, path+'webm\\'+files)
    if ".mp4" in files and not os.path.exists(path+'webm\\'+files):
        shutil.move(path+files, path+'webm\\'+files)
    if ".gif" in files and not os.path.exists(path+'gif\\'+files):
        shutil.move(path+files, path+'gif\\'+files)
