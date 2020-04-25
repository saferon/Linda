# Linda
Facial recognition script for organising folders of faces into subfolders containing matching faces

# How it works
In order for this to work, first you need to provide an already sorted collection of images and run that with pickler.py.
This will generate a pickle file, from there, this is then used by linda.py to go through an unsorted folder and move the images with matching faces into the directories that match that in the pickle file.
