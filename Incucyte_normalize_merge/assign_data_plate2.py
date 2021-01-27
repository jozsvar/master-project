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

parser.add_argument('--norm_file', nargs=1, type= str, default=sys.stdin, help = 'Path to normalized plate 2 file')
parser.add_argument('--D57_SCZ_SCZ_file', nargs=1, type= str, default=sys.stdin, help = 'Path to: D57_SCZline_SCZsyn.tsv')
parser.add_argument('--D57_SCZ_HC_file', nargs=1, type= str, default=sys.stdin, help = 'Path to: D57_SCZline_HCsyn.tsv')
parser.add_argument('--D57_HC_SCZ_file', nargs=1, type= str, default=sys.stdin, help = 'Path to: D57_HCline_SCZsyn.tsv')
parser.add_argument('--D57_HC_HC_file', nargs=1, type= str, default=sys.stdin, help = 'Path to: D57_HCline_HCsyn.tsv')

parser.add_argument('--letters_HC_2', nargs=1, type= str, default=sys.stdin, help = 'Letters for HC lines separated by comma as str: B,C,D,E')
parser.add_argument('--letters_SCZ_2', nargs=1, type= str, default=sys.stdin, help = 'Letters for SCZ lines separated by comma as str: F,G')
parser.add_argument('--numbers_SCZ', nargs=1, type= str, default=sys.stdin, help = 'Well numbers for SCZ SYN separated by comma as int: 2,3')
parser.add_argument('--numbers_HC', nargs=1, type= str, default=sys.stdin, help = 'Well numbers for HC SYN separated by comma as int: 8,9')

parser.add_argument('--outdir_results', nargs=1, type= str, default=sys.stdin, help = 'Path to output directory to results folder')


###FUNCTION####


def plate2_SCZ_SCZ(norm_df, D57_SCZ_SCZ_file, letters_SCZ_2, numbers_SCZ, outdir_results):
	'''gets all the D57 SCZ cell lines from plate 2 with SCZ SYN incubated - appends to existing file and creates new file
	'''
	D57_file = pd.read_csv(D57_SCZ_SCZ_file, sep='\t', encoding='utf8')
	
	extracted_rows = []

	for l in letters_SCZ_2: 
		for n in numbers_SCZ:
			#select specific well letters and numbers from dataframe 
			filter_rows = norm_df.loc[(norm_df['well_letter'] == l) & (norm_df['well_number'] == n)]
			#append to a list
			extracted_rows.append(filter_rows)


	#puts everything together from list 
	df = pd.concat(extracted_rows)

	new_df=D57_file.append(df, ignore_index=True)
	#create new dataframe 
	new_df.to_csv(outdir_results+'D57_SCZline_SCZsyn_1.tsv', index=False, sep='\t')
	
	print 'values added to D57 SCZ line + SCZ syn and new file was created'


def plate2_SCZ_HC(norm_df, D57_SCZ_HC_file, letters_SCZ_2, numbers_HC, outdir_results):
	'''gets all the D57 SCZ cell lines from plate 2 with HC SYN incubated - appends to existing file and creates new file
	'''
	D57_file = pd.read_csv(D57_SCZ_HC_file, sep='\t', encoding='utf8')
	
	extracted_rows = []

	for l in letters_SCZ_2: 
		for n in numbers_HC:
			#select specific well letters and numbers from dataframe 
			filter_rows = norm_df.loc[(norm_df['well_letter'] == l) & (norm_df['well_number'] == n)]
			#append to a list
			extracted_rows.append(filter_rows)


	#puts everything together from list 
	df = pd.concat(extracted_rows)

	new_df=D57_file.append(df, ignore_index=True)
	#create new dataframe 
	new_df.to_csv(outdir_results+'D57_SCZline_HCsyn_1.tsv', index=False, sep='\t')
	
	print 'values added to D57 SCZ line + HC syn and new file was created'


def plate2_HC_SCZ(norm_df, D57_HC_SCZ_file, letters_HC_2, numbers_SCZ, outdir_results):
	'''gets all the D57 HC cell lines from plate 2 with SCZ SYN incubated - appends to existing file and creates new file
	'''
	D57_file = pd.read_csv(D57_HC_SCZ_file, sep='\t', encoding='utf8')
	
	extracted_rows = []

	for l in letters_HC_2: 
		for n in numbers_SCZ:
			#select specific well letters and numbers from dataframe 
			filter_rows = norm_df.loc[(norm_df['well_letter'] == l) & (norm_df['well_number'] == n)]
			#append to a list
			extracted_rows.append(filter_rows)


	#puts everything together from list 
	df = pd.concat(extracted_rows)

	new_df=D57_file.append(df, ignore_index=True)
	#create new dataframe 
	new_df.to_csv(outdir_results+'D57_HCline_SCZsyn_1.tsv', index=False, sep='\t')
	
	print 'values added to D57 HC line + SCZ syn and new file was created'



def plate2_HC_HC(norm_df, D57_HC_HC_file, letters_HC_2, numbers_HC, outdir_results):
	'''gets all the D57 HC cell lines from plate 2 with HC SYN incubated - appends to existing file and creates new file
	'''
	D57_file = pd.read_csv(D57_HC_HC_file, sep='\t', encoding='utf8')
	
	extracted_rows = []

	for l in letters_HC_2: 
		for n in numbers_HC:
			#select specific well letters and numbers from dataframe 
			filter_rows = norm_df.loc[(norm_df['well_letter'] == l) & (norm_df['well_number'] == n)]
			#append to a list
			extracted_rows.append(filter_rows)


	#puts everything together from list 
	df = pd.concat(extracted_rows)

	new_df=D57_file.append(df, ignore_index=True)
	#create new dataframe 
	new_df.to_csv(outdir_results+'D57_HCline_HCsyn_1.tsv', index=False, sep='\t')
	
	print 'values added to D57 HC line + HC syn and new file was created'


####MAIN####

#Split args
args = parser.parse_args()

#input files to merge all files
norm_file=args.norm_file[0]
D57_SCZ_SCZ_file=args.D57_SCZ_SCZ_file[0]
D57_SCZ_HC_file=args.D57_SCZ_HC_file[0]
D57_HC_SCZ_file=args.D57_HC_SCZ_file[0]
D57_HC_HC_file=args.D57_HC_HC_file[0]

letters_HC_2=args.letters_HC_2[0].split(',')
letters_SCZ_2=args.letters_SCZ_2[0].split(',')
numbers_SCZ = np.array(args.numbers_SCZ[0].split(','),dtype='int32')
numbers_HC = np.array(args.numbers_HC[0].split(','),dtype='int32')

outdir_results=args.outdir_results[0]


norm_df = pd.read_csv(norm_file, sep='\t', encoding='utf8')
norm_df["time_point_x"].replace({'00d00h00m':'pre','00d00h15m':'pre','00d00h41m':'00:00','00d01h11m':'00:30','00d01h41m':'01:00','00d02h11m':'01:30','00d02h41m':'02:00','00d03h11m':'02:30','00d03h41m':'03:00','00d04h11m':'03:30','00d04h41m':'04:00','00d05h11m':'04:30','00d05h41m':'05:00','00d06h11m':'05:30','00d06h41m':'06:00','00d07h41m':'07:00','00d08h41m':'08:00','00d09h41m':'09:00','00d10h41m':'10:00','00d11h41m':'11:00','00d12h41m':'12:00','00d13h41m':'13:00','00d14h41m':'14:00','00d15h41m':'15:00','00d16h41m':'16:00','00d17h41m':'17:00','00d18h41m':'18:00','00d19h41m':'19:00','00d20h41m':'20:00','00d21h41m':'21:00','00d22h41m':'22:00','00d23h41m':'23:00','01d00h41m':'24:00'}, inplace=True)

#add plate 2 cell lines two the files created from plate 1
plate2_SCZ_SCZ(norm_df, D57_SCZ_SCZ_file, letters_SCZ_2, numbers_SCZ, outdir_results)
plate2_SCZ_HC(norm_df, D57_SCZ_HC_file, letters_SCZ_2, numbers_HC, outdir_results)
plate2_HC_SCZ(norm_df, D57_HC_SCZ_file, letters_HC_2, numbers_SCZ, outdir_results)
plate2_HC_HC(norm_df, D57_HC_HC_file, letters_HC_2, numbers_HC, outdir_results)












