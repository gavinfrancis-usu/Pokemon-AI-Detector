import os
import subprocess
import sys

#cd C:\Users\gavin\Desktop\School\Current-Courses\CS-5600\Homework\CS5600_6600_F21_Project02\yolov5
#print("\nTHe String is --> " , results_weights_directory , "\n")

epochs = 200
batch_size = 10 # just setting it so it doesn't freak out
conf_thres = 0.5

results_name = "squirtle-results"
data_path = r"C:\Users\gavin\Desktop\School\Current-Courses\CS-5600\Homework\CS5600_6600_F21_Project02\yolov5\data\pokemon.yaml"
test_source = r"C:\Users\gavin\Desktop\School\Current-Courses\CS-5600\Homework\CS5600_6600_F21_Project02\yolov5\datasets\pokemon\images\test"

train_data = ''
test_data = ''

for i in range(8):
    results_weights_directory = r"C:\Users\gavin\Desktop\School\Current-Courses\CS-5600\Homework\CS5600_6600_F21_Project02\yolov5\runs\train" + "\\" + (results_name + str(i+1)) + r"\weights\best.pt"

    if i == 0 or i == 1:

        img_size = 416
        batch_size = 16
        weights_directory = ''
    
        if i == 0:
            weights_directory = r"C:\Users\gavin\Desktop\School\Current-Courses\CS-5600\Homework\CS5600_6600_F21_Project02\yolov5\weights\yolov5s.pt"
            results_weights_directory = r"C:\Users\gavin\Desktop\School\Current-Courses\CS-5600\Homework\CS5600_6600_F21_Project02\yolov5\runs\train" + "\\" +  results_name + r"\weights\best.pt"

        elif i == 1:
            weights_directory = r"C:\Users\gavin\Desktop\School\Current-Courses\CS-5600\Homework\CS5600_6600_F21_Project02\yolov5\weights\yolov5m.pt"

        train_data = 'python train.py --img ' + str(img_size) + ' --batch ' + str(batch_size) + ' --epochs ' + str(epochs) + ' --data ' + data_path + ' --weights ' + weights_directory + ' --name ' + results_name + ' --cache'
        test_data = 'python detect.py --img ' + str(img_size) + ' --source ' + str(test_source) + ' --weights ' + results_weights_directory + ' --conf-thres ' + str(conf_thres)
        subprocess.run(train_data)
        subprocess.run(test_data)



    elif i == 2 or i == 3:
        img_size = 468
        weights_directory = ''

        if i == 2:
            batch_size = 16
            weights_directory = r"C:\Users\gavin\Desktop\School\Current-Courses\CS-5600\Homework\CS5600_6600_F21_Project02\yolov5\weights\yolov5s.pt"

        elif i == 3:
            batch_size = 14
            weights_directory = r"C:\Users\gavin\Desktop\School\Current-Courses\CS-5600\Homework\CS5600_6600_F21_Project02\yolov5\weights\yolov5m.pt"

        train_data = 'python train.py --img ' + str(img_size) + ' --batch ' + str(batch_size) + ' --epochs ' + str(epochs) + ' --data ' + data_path + ' --weights ' + weights_directory + ' --name ' + results_name + ' --cache'
        test_data = 'python detect.py --img ' + str(img_size) + ' --source ' + str(test_source) + ' --weights ' + results_weights_directory + ' --conf-thres ' + str(conf_thres)
        subprocess.run(train_data)
        subprocess.run(test_data)

    elif i == 4 or i == 5:
        img_size = 520
        weights_directory = ''

        if i == 4:
            batch_size = 14
            weights_directory = r"C:\Users\gavin\Desktop\School\Current-Courses\CS-5600\Homework\CS5600_6600_F21_Project02\yolov5\weights\yolov5s.pt"

        elif i == 5:
            batch_size = 10
            weights_directory = r"C:\Users\gavin\Desktop\School\Current-Courses\CS-5600\Homework\CS5600_6600_F21_Project02\yolov5\weights\yolov5m.pt"

        train_data = 'python train.py --img ' + str(img_size) + ' --batch ' + str(batch_size) + ' --epochs ' + str(epochs) + ' --data ' + data_path + ' --weights ' + weights_directory + ' --name ' + results_name + ' --cache'
        test_data = 'python detect.py --img ' + str(img_size) + ' --source ' + str(test_source) + ' --weights ' + results_weights_directory + ' --conf-thres ' + str(conf_thres)
        subprocess.run(train_data)
        subprocess.run(test_data)


    elif i == 6 or i == 7:
        img_size = 624
        weights_directory = ''

        if i == 6:
            batch_size = 14
            weights_directory = r"C:\Users\gavin\Desktop\School\Current-Courses\CS-5600\Homework\CS5600_6600_F21_Project02\yolov5\weights\yolov5s.pt"

        elif i == 7:
            batch_size = 8
            weights_directory = r"C:\Users\gavin\Desktop\School\Current-Courses\CS-5600\Homework\CS5600_6600_F21_Project02\yolov5\weights\yolov5m.pt"

        train_data = 'python train.py --img ' + str(img_size) + ' --batch ' + str(batch_size) + ' --epochs ' + str(epochs) + ' --data ' + data_path + ' --weights ' + weights_directory + ' --name ' + results_name + ' --cache'
        test_data = 'python detect.py --img ' + str(img_size) + ' --source ' + str(test_source) + ' --weights ' + results_weights_directory + ' --conf-thres ' + str(conf_thres)
        subprocess.run(train_data)
        subprocess.run(test_data)
    
