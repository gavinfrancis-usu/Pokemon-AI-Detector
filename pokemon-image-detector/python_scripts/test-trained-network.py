import os
import sys
import subprocess

conf_thres = sys.argv[1]

os.chdir('../')
cwd = os.getcwd()

operator_sign = ''
if '/' in cwd:
    operator_sign = '/'
else:
    operator_sign ='\\'

test_source = cwd + operator_sign + 'files_needed' + operator_sign + 'datasets' + operator_sign + 'all_pokemon-dataset' + operator_sign + 'images' + operator_sign +  'test' + operator_sign
weights_file_path = cwd + operator_sign + 'results-train' + operator_sign + 'all-pokemon' + operator_sign + 'all-pokemon-results' + operator_sign + 'weights' + operator_sign + 'best.pt'


cwd = cwd + operator_sign + 'yolov5'
os.chdir(cwd)

if operator_sign == '\\':
    subprocess.check_call(["python", "detect.py" , "--img" , "416" , "--source" , str(test_source), "--weights" , str(weights_file_path), "--conf-thres" , conf_thres], stdout=subprocess.PIPE)

if operator_sign == '/':
    subprocess.check_call(["python3", "detect.py" , "--img" , "416" , "--source" , str(test_source), "--weights" , str(weights_file_path), "--conf-thres" , conf_thres], stdout=subprocess.PIPE)

#test_data = 'python detect.py --img 416 --source ' + str(test_source) + ' --weights ' + weights_file_path + ' --conf-thres ' + str(conf_thres)
#subprocess.run(test_data)
