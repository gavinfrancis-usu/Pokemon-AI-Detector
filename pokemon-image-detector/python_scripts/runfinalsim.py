import os
import subprocess
import sys

epochs = 300
batch_size = 10 # just setting it so it doesn't freak out
conf_thres = 0.65

results_name = "all-pokemon-results"
data_path = r"C:\Users\gavin\Desktop\School\Current-Courses\CS-5600\Homework\CS5600_6600_F21_Project02\yolov5\data\pokemon.yaml"
test_source = r"C:\Users\gavin\Desktop\School\Current-Courses\CS-5600\Homework\CS5600_6600_F21_Project02\yolov5\datasets\pokemon\images\test"

train_data = ''
test_data = ''

for i in range(8):
    weights_directory = r"C:\Users\gavin\Desktop\School\Current-Courses\CS-5600\Homework\CS5600_6600_F21_Project02\yolov5\weights\yolov5m.pt"
    results_weights_directory = r"C:\Users\gavin\Desktop\School\Current-Courses\CS-5600\Homework\CS5600_6600_F21_Project02\yolov5\runs\train" + "\\" + (results_name + str(i+1)) + r"\weights\best.pt"

    if i == 0:
        img_size = 416
        batch_size = 16
        results_weights_directory = r"C:\Users\gavin\Desktop\School\Current-Courses\CS-5600\Homework\CS5600_6600_F21_Project02\yolov5\runs\train" + "\\" +  results_name + r"\weights\best.pt"

        train_data = 'python train.py --img ' + str(img_size) + ' --batch ' + str(batch_size) + ' --epochs ' + str(epochs) + ' --data ' + data_path + ' --weights ' + weights_directory + ' --name ' + results_name + ' --cache'
        test_data = 'python detect.py --img ' + str(img_size) + ' --source ' + str(test_source) + ' --weights ' + results_weights_directory + ' --conf-thres ' + str(conf_thres)
        subprocess.run(train_data)
        subprocess.run(test_data)



    elif i == 1:
        img_size = 468
        batch_size = 14

        train_data = 'python train.py --img ' + str(img_size) + ' --batch ' + str(batch_size) + ' --epochs ' + str(epochs) + ' --data ' + data_path + ' --weights ' + weights_directory + ' --name ' + results_name + ' --cache'
        test_data = 'python detect.py --img ' + str(img_size) + ' --source ' + str(test_source) + ' --weights ' + results_weights_directory + ' --conf-thres ' + str(conf_thres)
        subprocess.run(train_data)
        subprocess.run(test_data)

    elif i == 3:
        img_size = 520
        batch_size = 10

        train_data = 'python train.py --img ' + str(img_size) + ' --batch ' + str(batch_size) + ' --epochs ' + str(epochs) + ' --data ' + data_path + ' --weights ' + weights_directory + ' --name ' + results_name + ' --cache'
        test_data = 'python detect.py --img ' + str(img_size) + ' --source ' + str(test_source) + ' --weights ' + results_weights_directory + ' --conf-thres ' + str(conf_thres)
        subprocess.run(train_data)
        subprocess.run(test_data)


    elif i == 4:
        img_size = 624
        batch_size = 8

        train_data = 'python train.py --img ' + str(img_size) + ' --batch ' + str(batch_size) + ' --epochs ' + str(epochs) + ' --data ' + data_path + ' --weights ' + weights_directory + ' --name ' + results_name + ' --cache'
        test_data = 'python detect.py --img ' + str(img_size) + ' --source ' + str(test_source) + ' --weights ' + results_weights_directory + ' --conf-thres ' + str(conf_thres)
        subprocess.run(train_data)
        subprocess.run(test_data)
    
