'''
Created on Jun 4, 2020

@author: Jeremy Scheuerman
'''

# "D:\Documents\Programming\Pendant_Automation\Lucas_Docs";
# /home/jeremy/Documents/Pendant_automation/Lucas_Docs
import os, sys;
# get get os stuff and file mod functions
import mysql.connector;
from mysql.connector import (connection)
# get mysql stuff
import time;
import schedule;
# import for timer stuff
import logging;
# import for debugging
import shutil;
# move overflow files to 
import atexit;
# write code that happens if the script is terminated

cnct = connection.MySQLConnection(user='jscheuerman', password='L*KCy7d4Lxa2-r',
                                 host='10.200.0.33',
                                 database='employees')
# establish connection names are temporary until mysql is figured out


def do_everything():
    # put it all in a function
    working_path = "/home/jeremy/Documents/Pendant_automation/Lucas_Docs/this_file";  # replace with dir that 
    # path of python documents fold
    misplaced_path = "/home/jeremy/Documents/Pendant_automation/Lucas_Docs/misplaced";
    # path for files placed in the wrong folder
    os.chdir(working_path);
    # go to the directory
    home = os.getcwd();
    # store home
    save_path_location = "/home/jeremy/Documents/Pendant_automation/converter_tests/";
    # path to save new files to
    exists = False;
    # init3
    for fname in os.listdir('.'):
        print(fname)
        if fname.endswith('.DAT'):
            # do stuff on the file
            exists = True;
            # if its a .dat file then it exists
            break;
        else:
            exists = False;
            # or it dodsent
            moved = shutil.move(fname, misplaced_path);
            print("That file was not a .DAT file it has been moved to " + moved);
            # move files that re placed and don't have a .dat extension
    # do stuff if a file .true doesn't exist.
    if exists == True:
        orig_file_name = fname;  # insert fancy functions to get name of file
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


schedule.every(15).seconds.do(do_everything);
# do it every 10 seconds
while 1:
    schedule.run_pending();
    time.sleep(1);
    # don't run it 50 times over
    
atexit.register(cnct.close());
# makes sure the connection is always terminated if the script is terminated

