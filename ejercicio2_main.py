#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
from ejercicio2_funciones import convert_format, load_data_list, transform_data, load_output_file


def main():
    # establezco ubicacion de archivos en caso de no ser especificados
    input = os.path.dirname(os.path.abspath(__file__)) + os.sep + 'datos_data_engineer.tsv'
    output = os.path.dirname(os.path.abspath(__file__)) + os.sep + 'output_data_engineer.csv'

    # cambio el formato a utf-8 y la guardo en un buffer
    buffer = convert_format(input, output)
	
    # cargo la data proveniente de buffer en una lista para poder trabajar
    data = load_data_list(buffer)

    # transformo la data separandola con |
    load_data = transform_data(data)
    
	# cargo el archivo resultante
    load_output_file(load_data, output)
	
if __name__ == '__main__':
    main()