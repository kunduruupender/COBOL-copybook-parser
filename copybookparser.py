#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 15:06:30 2023

@author: kunduruupender
"""

import os


def removeBeforeAndAfterSeventyTwo(lines):
    data=[]
    
    for line in lines:
        if(line.__contains__("*") or line.startswith("*")):
            continue
        elif len(line) > 72:
            subline = line[6:72]
            data.append(subline)
        else:
            subline = line[6:]
            data.append(subline)
    return data

def duplicateField(lines):
    field_names = []
    
    for i,line in enumerate(lines):
        field_name_list = line.split()
        if len(field_name_list)>1:
            field_name = field_name_list[1]
            if field_name in field_names:
                new_field_name = field_name + "-" + str(i)
                lines[i] = line.replace(field_name, new_field_name)
            else:
                field_name.append(field_name)
    return lines

def redfination(lines):
    x=lines.split(".")
    
    filename = ''.join([i for i in x[0].split("-")[0] if not i.isdigit()])
    rectype=""
    
    #get pic(x)
    for data in x:
        if "05 " in data:
            rectype = data.split()[2] + ' ' + data.split()[3]
            break
    
    x.insert(1, f"\n\t\t02 {filename}-REC-TYPE " + rectype)
    
    detail_string = ""
    found_detail_at = 0
    header_string = ""
    
    for i,data in enumerate(x):
        if "02 " in data:
            found_detail_at +=1
            if found_detail_at ==2:
                header_string = data.split()[1]
                
            if found_detail_at == 2:
                detail_string = data
                x[i] = detail_string
                del x[i+1]
                del x[i+1]
                
            if found_detail_at == 3:
                detail_string = data
                x[i] = detail_string
                del x[i+1]
                del x[i+1]
                
            if found_detail_at == 4:
                detail_string = data
                x[i] = detail_string
                del x[i+1]
                del x[i+1]
                
        x[i] = x[i] +"."
    return x

def indentation(lines):
    data = []
    i=0
    space_temp = " "
    
    for line in lines:
        i+=1
        line = line.strip()
        if(line[0:2] == '01'):
            data.append(space_temp *7 + line)
        elif(line[0:2] == '02'):
            data.append(space_temp *11 +line)
        elif(line[0:2] == '05'):
            data.append(space_temp *14 +line)
        elif(line[0:2] == '10'):
            data.append(space_temp *17 +line)
        elif(line[0:2] == '15'):
            data.append(space_temp *20 +line)
        else:
            data.append(space_temp *17 + line)
    
    return data

def maxLengthSeventyTwo(lines, dir_path):
    outputfile = dir_path+ "/output.cpy"
    data = []
    
    for line in lines:
        if not line.strip().startswith("*"):
            if len(line)>72:
                line = keepBetweenSeventhandSeventySecond(line)
            data.append(line)
    cpy_content = "\n".join(data)
    with open(outputfile, "w") as the_file1:
        the_file1.write(f"{cpy_content}\n")

def keepBetweenSeventhandSeventySecond(line):
    leading_spaces = len(line) - len(line.strip())
    line_arr = line.split()
    first_line = " "*(leading_spaces-1)+(" ".join(line_arr[:2]))
    second_line = " "*(leading_spaces-1)+(" ".join(line_arr[2:]) + "\n")
    return "\n".join([first_line,second_line])
            

def copybookAsset():
    path = input("give path to your file")
    output_dir_path = os.path.dirname(path)
    path = path.strip()
    f = open(path, "r")
    lines = f.readlines()
    data_after_seventytwo = removeBeforeAndAfterSeventyTwo(lines)
    lines = duplicateField(data_after_seventytwo)
    line_str ="".join(lines)
    redefined_cpy = redfination(line_str)
    indentation_file = indentation(redefined_cpy)
    maxLengthSeventyTwo(indentation_file, output_dir_path)
    print("copybook parsed sucessfully")

copybookAsset()
        