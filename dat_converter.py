'''
Created on Jun 4, 2020

@author: Jeremy Scheuerman
'''

# "D:\Documents\Programming\Pendant_Automation\Lucas_Docs";
# /home/jeremy/Documents/Pendant_automation/Lucas_Docs
import os, sys;
# get get os stuff and file mod functions
import mysql.connector;
# get mysql stuff
import time;
import schedule;
# import for timer stuff
import logging;
# import for debugging

def do_everything():
    # put it all in a function
    working_path = "/home/jeremy/Documents/Pendant_automation/Lucas_Docs/this_file";  # replace with dir that 
    # path of python documents fold
    os.chdir(working_path);
    # go to the directory
    home = os.getcwd();
    # store home
    save_path_location = "/home/jeremy/Documents/Pendant_automation/converter_tests/";
    # path to save new files to
    for fname in os.listdir('.'):
        if fname.endswith('.DAT'):
            # do stuff on the file
            
            break
        else:
    # do stuff if a file .true doesn't exist.
    if exists == True:
        orig_file_name = "ASSIGNMENT-2020032214393416.DAT";  # insert fancy functions to get name of file
        temp_name = orig_file_name[:-3];
        # get variable for file name and var for path
        orig_file_path = working_path + "/" + orig_file_name;
        # path to delete file after job is done
        save_path = save_path_location + temp_name;
        # create save path name
        os.mkdir(save_path);
        # create new folder for dat files
        og_dat_file = open(orig_file_name, "r");
        # openfile
        all_lines = og_dat_file.readlines();
        # get read all lines variable
        num_lines = sum(1 for line in open(orig_file_name));
        # get number of lines in the file
        print("Number of files to be created " + str(num_lines));
        # print number of lines
        for j in range(num_lines):
            line_dump_data = all_lines[j];
            # get data from specific line 
            new_file_name = line_dump_data[21:35] + ".DAT";
            # get name for new dat file from line data 
            new_name_complete = os.path.join(save_path, new_file_name);
            # and name combined with save path
            new_file_data = line_dump_data;
            # get data to be added to the new dat file
            new_file = open(new_name_complete, "w");
            # Creates a new file from the temp vars
            new_file.write(new_file_data);
            new_file.close();
            # if file exists then exists is true
        os.remove(orig_file_path);
        # delete original file
    else:
        print("No file present");
        # acknowlege no file is there


schedule.every(10).seconds.do(do_everything);
# do it every 10 seconds
while 1:
    schedule.run_pending();
    time.sleep(1);
