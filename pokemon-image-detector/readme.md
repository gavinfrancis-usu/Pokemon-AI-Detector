--Instructions on Running Program / Additional Work Sources--

I trained my networks using YOLOv5.  From the training I was able to obtain trained networks from there saved in .pt files.
To detect test images we will need to install YOLOv5 and all the necessary packages are required.  I have provided two separate methods to install YOLOv5.   

Installing YOLOv5 with a Script:
- I have created a script that will install YOLOv5 and all of the requirements it needs to run.  
- To run the script, navigate to /python_scripts/installrequirements.py and run it using "python installrequirements.py.
- If it doesn't work or any errors are thrown install in manually.

Installing YOLOv5 Manually:
- Clone the Repository here: https://github.com/ultralytics/yolov5/
- cd into the yolov5 and run the following command: "pip install -r requirements.txt"
- There is additional information here if there is any issues: https://github.com/ultralytics/yolov5/


Now that YOLOv5 and the necessary requirements are installed we can start running my trained networks on test images.
In total there are 79 different test images and 1 test video that is approximately 2 minutes and 45 seconds long.


Running the Best Trained Network on Images and Videos with a Script:
- I have created a script that will run my trained networks on a series of test images and a video.
- To run the script, navigate to /python_scripts/test-trained-network.py and run it using "python test-trained-network.py <given_conf_thres>".
	- Example: 'python test-trained-network.py 0.65'
- After the detection is finished the results will be saved in "/yolov5/runs/detect/"
- If it doesn't work run it manually.


Running the Best Trained Network on Images and Videos Manually:
- Navigate to the yolov5 directory and verify that there is "detect.py".
- Run the following command: "python detect.py --img 416 --source <path_to_test_dataset> --weights <path_to_best.pt> --conf-thres <0.0-0.99>"
	- "--img <#>" is the sizes of the images
	- "--source <path>" this is the path to the images and video that will be trained
	- "--weights <path>" is the path to the weights file (trained network)
	- "--conf-thres <#>" if the accuracy is above the conf-thres then it will be displayed with a bounding box
- After the detection is finished the results will be saved in "/yolov5/runs/detect/"


Additional Places to sources:
- Final-Report: final-report.pdf
- RAW Result/Dataset Documentation: myresults.txt
- My saved Dataset: my_detect_results
- Github Repository: https://github.com/gavinfrancis-usu/Pokemon-AI-Detector which contains...
	- Contains all pokemon datasets, 
	- Contains all detection results, 
	- Contains all test results, 
	- Contains all python scripts I used to train

