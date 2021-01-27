#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import pandas as pd
import sys
import argparse
import pdb

###Arguments for argparse module###
parser = argparse.ArgumentParser(description = '''A program that merges all files to 1''')
#input files

parser.add_argument('--file_to_add', nargs=1, type= str, default=sys.stdin, help = 'Path to input of other files')
parser.add_argument('--final_file', nargs=1, type= str, default=sys.stdin, help = 'Path to input of final file')

parser.add_argument('--ID', nargs=1, type= str, default=sys.stdin, help = 'ID for the new ID coloumn as str')

parser.add_argument('--outfile_final', nargs=1, type= str, default=sys.stdin, help = 'Path to final output file')

####FUNCTION####
def add_data(final_file, file_to_add, ID):
	'''gets the file and sorts it by 'time_point_x'
	'''
	add_file = pd.read_csv(file_to_add, sep='\t', encoding='utf8')
	merge_file = pd.read_csv(final_file, sep='\t', encoding='utf8')
	#Insert an ID on Location 1, with coloumn name 'ID' and the values in this coloumn 
	add_file.insert(0, 'ID', ID)
	#extract 3 columns from the dataframe with their coloumn names
	df = add_file[['ID','well_id','well_letter','well_number','time_point_x','Normalized_area']]
	#sort by time_point_x
	df.sort_values(by=['time_point_x'], ascending=True)


	#merge with 'final_file'
	new=pd.concat([merge_file,df])
	
	new.to_csv(outfile_final, index=False, sep='\t')


####MAIN####

#Split args
args = parser.parse_args()

#input files to merge all files
file_to_add=args.file_to_add[0]
final_file=args.final_file[0]

ID=args.ID[0]

outfile_final=args.outfile_final[0]

#Run script
add_data(final_file, file_to_add, ID)

