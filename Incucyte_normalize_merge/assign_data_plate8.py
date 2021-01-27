#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import glob
import pandas as pd
import sys
import argparse
import numpy as np
import pdb


###Arguments for argparse module###
parser = argparse.ArgumentParser(description = '''A program that assigns groups''')

parser.add_argument('--norm_file', nargs=1, type= str, default=sys.stdin, help = 'Path to normalized plate 8 file')
parser.add_argument('--D105_SCZ_SCZ_dead_file', nargs=1, type= str, default=sys.stdin, help = 'Path to: D105_SCZline_SCZsyn_dead.tsv')
parser.add_argument('--D105_SCZ_HC_file', nargs=1, type= str, default=sys.stdin, help = 'Path to: D105_SCZline_HCsyn_1.tsv')

parser.add_argument('--letters_SCZ', nargs=1, type= str, default=sys.stdin, help = 'Letters for SCZ lines separated by comma as str: B,C')
parser.add_argument('--numbers_SCZ', nargs=1, type= str, default=sys.stdin, help = 'Well numbers for SCZ SYN separated by comma as int: 2,3')
parser.add_argument('--numbers_HC', nargs=1, type= str, default=sys.stdin, help = 'Well numbers for HC SYN separated by comma as int: 6,7')

parser.add_argument('--outdir_results', nargs=1, type= str, default=sys.stdin, help = 'Path to output directory to results folder')


###FUNCTION####


def plate8_SCZ_SCZ_dead(norm_df, D105_SCZ_SCZ_dead_file, letters_SCZ, numbers_SCZ, outdir_results):
	'''gets all the D105 SCZ cell lines from plate 6 with SCZ SYN incubated and cells died - creates a new file for those 
	'''
	D105_file = pd.read_csv(D105_SCZ_SCZ_dead_file, sep='\t', encoding='utf8')
	
	extracted_rows = []

	for l in letters_SCZ: 
		for n in numbers_SCZ:
			#select specific well letters and numbers from dataframe 
			filter_rows = norm_df.loc[(norm_df['well_letter'] == l) & (norm_df['well_number'] == n)]
			#append to a list
			extracted_rows.append(filter_rows)


	#puts everything together from list 
	df = pd.concat(extracted_rows)

	new_df=D105_file.append(df, ignore_index=True)
	#create new dataframe 
	new_df.to_csv(outdir_results+'D105_SCZline_SCZsyn_dead_1.tsv', index=False, sep='\t')
	
	print 'values added to D105 SCZ line + SCZ syn (dead) and new file was created'



def plate8_SCZ_HC(norm_df, D105_SCZ_HC_file, letters_SCZ, numbers_HC, outdir_results):
	'''gets all the D105 SCZ cell lines from plate 6 with HC SYN incubated - appends to existing file and creates new file
	'''
	D105_file = pd.read_csv(D105_SCZ_HC_file, sep='\t', encoding='utf8')
	
	extracted_rows = []

	for l in letters_SCZ: 
		for n in numbers_HC:
			#select specific well letters and numbers from dataframe 
			filter_rows = norm_df.loc[(norm_df['well_letter'] == l) & (norm_df['well_number'] == n)]
			#append to a list
			extracted_rows.append(filter_rows)


	#puts everything together from list 
	df = pd.concat(extracted_rows)

	new_df=D105_file.append(df, ignore_index=True)
	#create new dataframe 
	new_df.to_csv(outdir_results+'D105_SCZline_HCsyn_2.tsv', index=False, sep='\t')
	
	print 'values added to D105 SCZ line + HC syn and new file was created'


####MAIN####

#Split args
args = parser.parse_args()

#input files to merge all files
norm_file=args.norm_file[0]
D105_SCZ_SCZ_dead_file=args.D105_SCZ_SCZ_dead_file[0]
D105_SCZ_HC_file=args.D105_SCZ_HC_file[0]

letters_SCZ=args.letters_SCZ[0].split(',')
numbers_SCZ = np.array(args.numbers_SCZ[0].split(','),dtype='int32')
numbers_HC = np.array(args.numbers_HC[0].split(','),dtype='int32')

outdir_results=args.outdir_results[0]

norm_df = pd.read_csv(norm_file, sep='\t', encoding='utf8')
norm_df["time_point_x"].replace({'00d00h00m': 'pre','00d00h18m':'00:00','00d00h48m':'00:30','00d01h18m':'01:00','00d01h48m':'01:30','00d02h18m':'02:00','00d02h48m':'02:30','00d03h18m':'03:00','00d03h48m':'03:30','00d04h18m':'04:00','00d04h48m':'04:30','00d05h18m':'05:00','00d05h48m':'05:30','00d06h18m':'06:00','00d07h18m':'07:00','00d08h18m':'08:00','00d09h18m':'09:00','00d10h18m':'10:00','00d11h18m':'11:00','00d12h18m':'12:00','00d13h18m':'13:00','00d14h18m':'14:00','00d15h18m':'15:00','00d16h18m':'16:00','00d17h18m':'17:00','00d18h18m':'18:00','00d19h18m':'19:00','00d20h18m':'20:00','00d21h18m':'21:00','00d22h18m':'22:00','00d23h18m':'23:00','01d00h18m':'24:00'}, inplace=True)

#add plate 8 cell lines two the files created from plate 4 + dead_file 
plate8_SCZ_SCZ_dead(norm_df, D105_SCZ_SCZ_dead_file, letters_SCZ, numbers_SCZ, outdir_results)
plate8_SCZ_HC(norm_df, D105_SCZ_HC_file, letters_SCZ, numbers_HC, outdir_results)


