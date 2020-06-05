'''
Created on Jun 4, 2020

@author: Jeremy Scheuerman
'''
# creates a new file in my python files directory
import os, sys;
# get get os stuff
home = os.getcwd();
# store hom
og_dat_file="example.dat";
#get name of dat file
path = "/mnt/D/Documents/Programming/Pendant_Automation/Lucas_Docs/ASSIGNMENT-2020032214393416.DAT";
# path of python documents fold
os.chdir(path);
# go to the directory
line_dump_data=[];
#arrays to store the full line of text from the
#dat file to then be modified with string functions and changed


num_lines = sum(1 for line in open(og_dat_file));
#get number of lines in the file
for j in num_lines:
    line_dump_data[j]=og_dat_file.readline(j);
    #get raw data to be split up
    new_file_name="insert fancy string indexing function here on line dump data";
    #get name for new dat file
    new_file_data="Insert more fancy string shit here to be added to the dat file";
    #get data to be added to the new dat file
    new_file = open(new_file_name, "x");
    # Creates a new file from the one stored in the index of the array
    with open(new_file, 'w') as fp: 
        pass
        # To write data to new file uncomment 
        fp.write(file_data);
        

#dat amount is the amount of .dat files in the list
new_file_path = path  + name;
# create variable with new file name;
new_file = open(name, "x");
# create new file
os.chdir(home);

# return home

  # fdsfds


