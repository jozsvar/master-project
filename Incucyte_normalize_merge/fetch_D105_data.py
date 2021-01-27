#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###Merge files 

import os
import glob
import pandas as pd
import sys
import argparse
import numpy as np
import pdb


###Arguments for argparse module###
parser = argparse.ArgumentParser(description = '''A program that gets the data from Plate 4 and creates a new file''')

parser.add_argument('--norm_file', nargs=1, type= str, default=sys.stdin, help = 'Path normalized file from plate 4')
parser.add_argument('--letters_SCZ', nargs=1, type= str, default=sys.stdin, help = 'Letters for SCZ lines separated by comma as str: B')
parser.add_argument('--letters_HC', nargs=1, type= str, default=sys.stdin, help = 'Letters for HC lines separated by comma as str: C,D,E,G')
parser.add_argument('--numbers_SCZ', nargs=1, type= str, default=sys.stdin, help = 'Well numbers for SCZ SYN separated by comma as int: 2,3')
parser.add_argument('--numbers_HC', nargs=1, type= str, default=sys.stdin, help = 'Well numbers for HC SYN separated by comma as int: 8,9')

parser.add_argument('--outdir_results', nargs=1, type= str, default=sys.stdin, help = 'Path to output directory to results folder')


###FUNCTION####

def fetch_SCZ_SCZ(norm_df, letters_SCZ, numbers_SCZ, outdir_results):
	'''gets all the D105 SCZ cell lines from plate 1 with SCZ SYN incubated - creates new file
	'''
	
	extracted_rows = []

	for l in letters_SCZ: 
		for n in numbers_SCZ:
			#select specific well letters and numbers from dataframe 
			filter_rows = norm_df.loc[(norm_df['well_letter'] == l) & (norm_df['well_number'] == n)]
			#append to a list
			extracted_rows.append(filter_rows)


	#puts everything together from list 
	new_df = pd.concat(extracted_rows)
	#create new dataframe 
	new_df.to_csv(outdir_results+'D105_SCZline_SCZsyn.tsv', index=False, sep='\t')
	
	
	print 'SCZ-SCZ-105 file created'


def fetch_SCZ_HC(norm_df, letters_SCZ, numbers_HC, outdir_results):
	'''gets all the D105 SCZ cell lines from plate 1 with HC SYN incubated - creates new file
	'''
	
	extracted_rows = []

	for l in letters_SCZ: 
		for n in numbers_HC:
			#select specific well letters and numbers from dataframe 
			filter_rows = norm_df.loc[(norm_df['well_letter'] == l) & (norm_df['well_number'] == n)]
			#append to a list
			extracted_rows.append(filter_rows)


	#puts everything together from list 
	new_df = pd.concat(extracted_rows)
	#create new dataframe 
	new_df.to_csv(outdir_results+'D105_SCZline_HCsyn.tsv', index=False, sep='\t')
	
	
	print 'SCZ-HC-105 file created'


def fetch_HC_SCZ(norm_df, letters_HC, numbers_SCZ, outdir_results):
	'''gets all the D105 HC cell lines from plate 1 with SCZ SYN incubated - creates new file
	'''
	
	extracted_rows = []

	for l in letters_HC: 
		for n in numbers_SCZ:
			#select specific well letters and numbers from dataframe 
			filter_rows = norm_df.loc[(norm_df['well_letter'] == l) & (norm_df['well_number'] == n)]
			#append to a list
			extracted_rows.append(filter_rows)


	#puts everything together from list 
	new_df = pd.concat(extracted_rows)
	#create new dataframe 
	new_df.to_csv(outdir_results+'D105_HCline_SCZsyn.tsv', index=False, sep='\t')
	
	
	print 'HC-SCZ-105 file created'


def fetch_HC_HC(norm_df, letters_HC, numbers_HC, outdir_results):
	'''gets all the D105 HC cell lines from plate 1 with HC SYN incubated - creates new file
	'''
	
	extracted_rows = []

	for l in letters_HC: 
		for n in numbers_HC:
			#select specific well letters and numbers from dataframe 
			filter_rows = norm_df.loc[(norm_df['well_letter'] == l) & (norm_df['well_number'] == n)]
			#append to a list
			extracted_rows.append(filter_rows)


	#puts everything together from list 
	new_df = pd.concat(extracted_rows)
	#create new dataframe 
	new_df.to_csv(outdir_results+'D105_HCline_HCsyn.tsv', index=False, sep='\t')
	
	
	print 'HC-HC-D105 file created'



####MAIN####
#Split args
args = parser.parse_args()
#input files
norm_file = args.norm_file[0]
letters_SCZ = args.letters_SCZ[0].split(',')
letters_HC = args.letters_HC[0].split(',')
numbers_SCZ = np.array(args.numbers_SCZ[0].split(','),dtype='int32')
numbers_HC = np.array(args.numbers_HC[0].split(','),dtype='int32')

#output files
outdir_results = args.outdir_results[0]

norm_df = pd.read_csv(norm_file, sep='\t', encoding='utf8')
norm_df["time_point_x"].replace({'00d00h00m': 'pre','00d00h27m':'00:00','00d00h57m':'00:30','00d01h27m':'01:00','00d01h57m':'01:30','00d02h27m':'02:00','00d02h57m':'02:30','00d03h27m':'03:00','00d03h57m':'03:30','00d04h27m':'04:00','00d04h57m':'04:30','00d05h27m':'05:00','00d05h57m':'05:30','00d06h27m':'06:00','00d07h27m':'07:00','00d08h27m':'08:00','00d09h27m':'09:00','00d10h27m':'10:00','00d11h27m':'11:00','00d12h27m':'12:00','00d13h27m':'13:00','00d14h27m':'14:00','00d15h27m':'15:00','00d16h27m':'16:00','00d17h27m':'17:00','00d18h27m':'18:00','00d19h27m':'19:00','00d20h27m':'20:00','00d21h27m':'21:00','00d22h27m':'22:00','00d23h27m':'23:00','01d00h27m':'24:00'}, inplace=True)

#create new files with different conditions for Dissociation time point D57 
fetch_SCZ_SCZ(norm_df, letters_SCZ, numbers_SCZ, outdir_results)
fetch_SCZ_HC(norm_df, letters_SCZ, numbers_HC, outdir_results)
fetch_HC_SCZ(norm_df, letters_HC, numbers_SCZ, outdir_results)
fetch_HC_HC(norm_df, letters_HC, numbers_HC, outdir_results)