#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Average the numbers that are in the same well + repitition

import os
import pandas as pd
import pdb
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import sys
import argparse

file = '/Users/Judit/Documents/TRIAL_FINAL_ANALYSIS_2/normalized.tsv'

###Arguments for argparse module###
parser = argparse.ArgumentParser(description = '''merges each picture from each well''')

parser.add_argument('--file', nargs=1, type= str, default=sys.stdin, help = 'Path normalized file')
parser.add_argument('--letter', nargs=1, type= str, default=sys.stdin, help = 'Letters for SCZ lines separated by comma as str: B,C,D,E,F')
parser.add_argument('--numbers1', nargs=1, type= str, default=sys.stdin, help = 'Well numbers for SCZ SYN separated by comma as int: 2,3')
parser.add_argument('--numbers2', nargs=1, type= str, default=sys.stdin, help = 'Well numbers for HC SYN separated by comma as int: 8,9 or 6,7')
parser.add_argument('--plate', nargs=1, type= str, default=sys.stdin, help = 'Plate ID')

parser.add_argument('--outdir', nargs=1, type= str, default=sys.stdin, help = 'Path to output directory to results folder')

###FUNCTIONS###

def merge_SCZ(file, letter, numbers1, plate):
	df = pd.read_csv(file, sep='\t', encoding='utf8')

	new_df = []
	merged = []

	#selects rows with same letters and numbers
	for l in letter:
		for n in numbers1:
			df1 = df.loc[(df['well_letter']==l)]
			df2 = df1.loc[df['well_number']== n]
			new_df.append(df2)

			df2 = pd.concat(new_df)

			#calculates the mean of the selected rows grouped by time point 
			mean = df2.groupby('time_point_x')['Normalized_area'].mean().reset_index()
			#inserts new coloumns to be able to identify the lines 
			mean.insert(0, 'well_id', plate)
			mean.insert(1, 'well_letter', l)
			mean.insert(2, 'well_number', n)
			mean.insert(3, 'SYN', 'SCZ')

			merged.append(mean)


	end_file_SCZ=pd.concat(merged)

	return end_file_SCZ


def merge_HC(file, letter, numbers2, plate):
	df = pd.read_csv(file, sep='\t', encoding='utf8')

	new_df = []
	merged = []
	
	#selects rows with same letters and numbers
	for l in letter:
		for n in numbers2:
			df1 = df.loc[(df['well_letter']==l)]
			df2 = df1.loc[df['well_number']== n]
			new_df.append(df2)
			
			df2 = pd.concat(new_df)
			#calculates the mean of the selected rows grouped by time point 
			mean = df2.groupby('time_point_x')['Normalized_area'].mean().reset_index()
			#inserts new coloumns to be able to identify the lines 
			mean.insert(0, 'well_id', plate)
			mean.insert(1, 'well_letter', l)
			mean.insert(2, 'well_number', n)
			mean.insert(3, 'SYN', 'HC')

			merged.append(mean)

	end_file_HC=pd.concat(merged)

	return end_file_HC

def merge_all(end_file_HC, end_file_SCZ, outdir):
	'''merge the 2 files and create 1 final file with the merged cell lines 
	'''
	frames = [end_file_HC, end_file_SCZ]
	merged = pd.concat(frames)

	merged.to_csv(outdir+'normalized_averaged.tsv', index=False, sep='\t')


###MAIN###
#Split args
args = parser.parse_args()
#input files
file = args.file[0]
letter = args.letter[0].split(',')
numbers1 = np.array(args.numbers1[0].split(','),dtype='int32')
numbers2 = np.array(args.numbers2[0].split(','),dtype='int32')
plate=args.plate[0]

#output files
outdir = args.outdir[0]
	
#run functions
end_file_SCZ=merge_SCZ(file, letter, numbers1, plate)
end_file_HC=merge_HC(file, letter, numbers2, plate)
merge_all(end_file_HC, end_file_SCZ, outdir)
