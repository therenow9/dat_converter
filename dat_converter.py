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
'''
cnct = connection.MySQLConnection(user='jscheuerman', password='L*KCy7d4Lxa2-r',
                                 host='10.200.0.33',
                                 database='temp')
                                 '''
                                 
cnct = connection.MySQLConnection(user='pendant', passwd='password',
                                 host='127.0.0.1')
                                 
# establish connection names are temporary until mysql is figured out

mycursor = cnct.cursor();
# get cursor


class obj_dat:
    # create object for easier organization and database management
    # here are the fields for the mysql table
    line_dump = "";
    # place holder for line dump dat
    rec_id = "        ";
    # record identifier
    # max length 8 
    route_num = "      ";
    # route number
    # max length 6
    stop_num = "    ";
    # stop number
    # max length 4
    container_id = "               ";
    # specific container for this pick 
    # max length 15
    assign_id = "                         ";
    # assignment id for container
    # max length 25
    pick_area = "      ";
    # concotatenation of 3 digit stype and 3 digit pick area 
    # max length of 6
    pick_type = "          ";
    # for full cas a description will be sent if no description it will just say full case
    # for split case it will always say split case
    # max length of 10
    juris = "      ";
    # neede for cig stamping, if not cigs then its spaces, 
    # max length of 6
    carton_num = "  ";
    # number of cigs in container, if not , spaces
    # max length 2


def dat_table_create(table_name):
    # define cursor
    mytable = "CREATE TABLE " + table_name + "\
     (Record_Identifier CHAR(8),Route_Number CHAR(6),\
    Stop_Number CHAR(4),Container_Id CHAR(15),Assignment_Id CHAR(25),\
    Pick_Area CHAR(6),Pick_Type CHAR(10),Jurisdiction CHAR(6),\
    Cartons_Number CHAR(2))";
    # create table for this file
    mycursor.execute(mytable);
    cnct.commit();
    # create table and commit to database


def dat_assign(obj_dat):
    # split strings and assign them to dat files
    tem = obj_dat.line_dump;
    # get line dump data
    obj_dat.rec_id = tem[0:8];
    obj_dat.route_num = tem[9:15];
    obj_dat.stop_num = tem[16:20];
    obj_dat.container_id = tem[21:36];
    obj_dat.assign_id = tem[37:62];
    obj_dat.pick_area = tem[63:69];
    obj_dat.pick_type = tem[70:80];
    obj_dat.juris = tem[81:87];
    obj_dat.carton_num = tem[88:90];
    # assign all fields for sql insertion
    return obj_dat;


def dat_test(obj_dat):
    # test values by printing them
    print(obj_dat.line_dump);
    print(obj_dat.rec_id + '\n' + 
    obj_dat.route_num + '\n' + 
    obj_dat.stop_num + '\n' + 
    obj_dat.container_id + '\n' + 
    obj_dat.assign_id + '\n' + 
    obj_dat.pick_area + '\n' + 
    obj_dat.pick_type + '\n' + 
    obj_dat.juris + '\n' + 
    obj_dat.carton_num);


def dat_insert(obj_dat, table_name):
    sql = "INSERT INTO " + table_name + " (Record_Identifier,Route_Number,\
    Stop_Number,Container_Id,Assignment_Id,Pick_Area,Pick_Type,\
    Jurisdiction,Cartons_Number) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)";
    # setup table insertion
    val = (obj_dat.rec_id, obj_dat.route_num, obj_dat.stop_num, obj_dat.container_id, obj_dat.assign_id, obj_dat.pick_area, obj_dat.juris, obj_dat.carton_num);
    # setup values for insertion
    mycursor.execute(sql, val);
    # insert the data into the table
    cnct.commit();
    # commit to database
    print(mycursor.rowcount, "data inserted");
    # confirm data added


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
        dat_table_create(temp_name);
        # create new table
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
            temp_dat = obj_dat();
            # create dat object for sql insertion
            temp_dat.line_dump = line_dump_data;
            temp_dat = dat_assign(temp_dat);
            # assing values for sql insertion
            # dat_test(temp_dat);
            dat_insert(temp_dat, temp_name);
            # insert data into mysql database
        os.remove(orig_file_path);
        # delete original file
    else:
        print("No file present");
        # acknowlege no file is there


schedule.every(7).seconds.do(do_everything);
# do it every 10 seconds
while 1:
    schedule.run_pending();
    time.sleep(1);
    # don't run it 50 times over
atexit.register(cnct.close);
# makes sure the connection is always terminated if the script is terminated

