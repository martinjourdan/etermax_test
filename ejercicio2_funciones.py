#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import io
import codecs
import commands
import click
import chardet


def convert_format(input, output):

    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

    data = open(input, 'rb').read()
    result = chardet.detect(data)
    char_enc = result['encoding']
    stream = codecs.open(input, 'r', char_enc)
    output = codecs.open(ROOT_DIR + os.sep + "file_temp", 'w', 'utf-8')
    for l in stream:
        output.write(l)
    stream.close()
    output.close()
    file_out = codecs.open(ROOT_DIR + os.sep +"file_temp", 'r', 'utf-8')
    buffer=file_out.read()
    file_out.close()
    os.remove(ROOT_DIR + os.sep +"file_temp")
    return buffer
	
	
def load_data_list(buffer):
    buffer_list = []
    string_list = ''
    data = []
    for string in buffer:
        if string=='\n':
            data.append(string_list)
            string_list=''
        else:
            string_list=string_list + string.encode('utf-8')
    data.append(string_list)
    return data
	
def transform_data(data):
    load_data=[]
    line_count = 0
    for row in data:
        if line_count == 0:
            row=row.split("\t")
            len_data=(row.__len__())
            line_count += 1
        else:
            row = row.split("\t")
            if not(len(row)==len_data):
                row=[]
            line_count += 1
        if len(row)>0:
            datarow = u''
            for value in row:
                if row.index(value) < (len_data - 1):
                    datarow = datarow + value.strip() + '|'
                else:
                    datarow = datarow + value.strip()
                    load_data.append(datarow)
    return load_data

def load_output_file(load_data, output):
    file = io.open(output, "w", encoding='utf-8')
    file.writelines("\n".join(load_data))
    if (file):
		print("El archivo 'output_data_engineer'.csv fue cargado exitosamente")

	
