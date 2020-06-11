'''
Created on Jun 4, 2020

@author: Jeremy Scheuerman
'''

# "D:\Documents\Programming\Pendant_Automation\Lucas_Docs";
# /home/jeremy/Documents/Pendant_automation/Lucas_Docs

import os, sys;
import mysql.connector;
# get get os stuff
import logging;
# import for debugging

working_path = "/home/jeremy/Documents/Pendant_automation/Lucas_Docs";#replace with dir that 
# path of python documents fold
save_path = "/home/jeremy/Documents/Pendant_automation/converter_tests";
# path to save new files to
os.chdir(working_path);
# go to the directory
home = os.getcwd();
# store home
orig_file_name = "ASSIGNMENT-2020032214393416.DAT";
# get variable for file name 
og_dat_file = open(orig_file_name, "r");
# openfile
all_lines = og_dat_file.readlines();
# get read all lines variable
num_lines = sum(1 for line in open(orig_file_name));
# get number of lines in the file
print("Number of files to be created "+str(num_lines));
#print number of lines
for j in range(num_lines):
    line_dump_data = all_lines[j];
    # get data from specific line 
    new_file_name = line_dump_data[21:35]+".DAT";
    # get name for new dat file from line data 
    new_name_complete=os.path.join(save_path,new_file_name);
    #and name combined with save path
    new_file_data = line_dump_data;
    # get data to be added to the new dat file
    new_file = open(new_name_complete, "w");
    # Creates a new file from the temp vars
    new_file.write(new_file_data);
    new_file.close();
    '''
    with open(new_file, 'w') as fp: 
        pass
        # To write data to new file uncomment 
        fp.write(new_file_data);
        '''
os.chdir(home);
# return home

