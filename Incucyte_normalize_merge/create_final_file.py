#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import pandas as pd
import sys
import argparse
import pdb

###Arguments for argparse module###
parser = argparse.ArgumentParser(description = '''A program that creates a final file''')
#input files
parser.add_argument('--sort_data_file', nargs=1, type= str, default=sys.stdin, help = 'Path to input of D57_SCZ_SCZ_file')
parser.add_argument('--ID', nargs=1, type= str, default=sys.stdin, help = 'ID for the new ID coloumn as str')

#output file
parser.add_argument('--outfile_final', nargs=1, type= str, default=sys.stdin, help = 'Path to final output file')


####FUNCTION####
def sort_data(sort_data_file, ID):
	'''gets the file and sorts it by 'time_point_x'
	'''
	sort_file = pd.read_csv(sort_data_file, sep='\t', encoding='utf8')
	#Insert an ID on Location 1, with coloumn name 'ID' and the values in this coloumn 
	sort_file.insert(0, 'ID', ID)
	#extract 3 columns from the dataframe with their coloumn names
	df = sort_file[['ID','well_id','well_letter','well_number','time_point_x','Normalized_area']]
	#sort by time_point_x
	df.sort_values(by=['time_point_x'], ascending=True)
	#Save into a new file
	df.to_csv(outfile_final, index=False, sep='\t')

	print 'file was created'


####MAIN####

#Split args
args = parser.parse_args()

#input files to merge all files
sort_data_file=args.sort_data_file[0]
ID=args.ID[0]

outfile_final=args.outfile_final[0]

#Run script
sort_data(sort_data_file, ID)






