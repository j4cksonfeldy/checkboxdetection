import os
import sys

sys.path.append('C:\Users\jackson.feldman\TF2\models\research')

args = sys.argv
directory = args[1]
protoc_path = args[2]
for file in os.listdir(directory):
    if file.endswith(".proto"):
        os.system(protoc_path+" "+directory+"/"+file+" --python_out=.")