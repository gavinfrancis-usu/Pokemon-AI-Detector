import os
import subprocess
import sys
import shutil

# cd C:\Users\gavin\Desktop\School\Current-Courses\CS-5600\Homework\CS5600_6600_F21_Project02

cwd = os.getcwd()

operator_sign = ''
if '/' in cwd:
    operator_sign = '/'
else:
    operator_sign ='\\'


print("\nInstalling YOLOv5 and Requirements...\n")

subprocess.run('git clone https://github.com/ultralytics/yolov5')
cwd = cwd + operator_sign + 'yolov5'
os.chdir(cwd)
print("I am here: " , os.getcwd())
subprocess.run('pip install -r requirements.txt')

#os.mkdir('datasets')
os.mkdir('weights')

#datasets_path = cwd + operator_sign + 'datasets'
weights_path = cwd + operator_sign + 'weights'

os.chdir('../')
cwd = os.getcwd() + operator_sign + 'trained_weights'
os.chdir(cwd)

weight_file = os.getcwd() + operator_sign + 'best.pt'

shutil.copyfile(weight_file, weights_path)

print("I am here: " , os.getcwd())