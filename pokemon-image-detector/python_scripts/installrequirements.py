import os
import subprocess
import sys
import shutil

os.chdir('../')
cwd = os.getcwd()

operator_sign = ''
if '/' in cwd:
    operator_sign = '/'
else:
    operator_sign ='\\'

cwd = os.getcwd()

print("\nInstalling YOLOv5 and Requirements...\n")

subprocess.check_call(["git", "clone", "https://github.com/ultralytics/yolov5"])

cwd = cwd + operator_sign + 'yolov5'
os.chdir(cwd)

print(".\n.\n.")

process2 = subprocess.Popen(["pip", "install" , "-r" , "requirements.txt"], stdout=subprocess.PIPE)
output2 = process2.communicate()[0]

print("\nInstalling YOLOv5 and Requirements are COMPLETE!!...\n")