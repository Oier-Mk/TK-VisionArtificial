import os
import glob

path = '/Users/mentxaka/Documents/Y - Trabajo/TK - VisionArtificial/FaceBlur/data/train/*'

for filename in glob.glob(path):
    if filename.split('.')[-1] == "txt":
        os.remove(filename)