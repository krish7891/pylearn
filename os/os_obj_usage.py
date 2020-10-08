import os

PATH="/home/pi/learning/pylearn/os/os_obj_usage.py"


#Example of basename
base_name = os.path.basename(PATH)
print "Usage of base name : " + base_name

dir_name = os.path.dirname(PATH)
print "Usage of dir name : " + dir_name

abs_path = os.path.isabs(PATH)
print "Check if path is absolute : "
print abs_path

is_dir_path = os.path.isdir(PATH)
print "check path is directory?"
print is_dir_path

print "Check path is file : "
is_file_path = os.path.isfile(PATH)
print is_file_path
