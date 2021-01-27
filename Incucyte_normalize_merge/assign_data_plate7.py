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

parser.add_argument('--norm_file', nargs=1, type= str, default=sys.stdin, help = 'Path to normalized plate 7 file')
parser.add_argument('--D57_SCZ_SCZ_file', nargs=1, type= str, default=sys.stdin, help = 'Path to: D57_SCZline_SCZsyn_2.tsv')
parser.add_argument('--D57_SCZ_HC_file', nargs=1, type= str, default=sys.stdin, help = 'Path to: D57_SCZline_HCsyn_2.tsv')

parser.add_argument('--D105_HC_SCZ_file', nargs=1, type= str, default=sys.stdin, help = 'Path to: D105_HCline_SCZsyn_2.tsv')
parser.add_argument('--D105_HC_HC_file', nargs=1, type= str, default=sys.stdin, help = 'Path to: D105_HCline_HCsyn_2.tsv')

parser.add_argument('--letters_SCZ', nargs=1, type= str, default=sys.stdin, help = 'Letters for SCZ lines separated by comma as str: B,C,D')
parser.add_argument('--letters_HC', nargs=1, type= str, default=sys.stdin, help = 'Letters for HC lines separated by comma as str: E')
parser.add_argument('--numbers_SCZ', nargs=1, type= str, default=sys.stdin, help = 'Well numbers for SCZ SYN separated by comma as int: 2,3')
parser.add_argument('--numbers_HC', nargs=1, type= str, default=sys.stdin, help = 'Well numbers for HC SYN separated by comma as int: 6,7')


parser.add_argument('--outdir_results', nargs=1, type= str, default=sys.stdin, help = 'Path to output directory to results folder')



###FUNCTION####

def plate7_SCZ_SCZ(norm_df, D57_SCZ_SCZ_file, letters_SCZ, numbers_SCZ, outdir_results):
	'''gets all the D57 SCZ cell lines from plate 7 with SCZ SYN incubated - appends to existing file and creates new file
	'''
	D57_file = pd.read_csv(D57_SCZ_SCZ_file, sep='\t', encoding='utf8')
	
	extracted_rows = []

	for l in letters_SCZ: 
		for n in numbers_SCZ:
			#select specific well letters and numbers from dataframe 
			filter_rows = norm_df.loc[(norm_df['well_letter'] == l) & (norm_df['well_number'] == n)]
			#append to a list
			extracted_rows.append(filter_rows)


	#puts everything together from list 
	df = pd.concat(extracted_rows)

	new_df=D57_file.append(df, ignore_index=True)
	#create new dataframe 
	new_df.to_csv(outdir_results+'D57_SCZline_SCZsyn_3.tsv', index=False, sep='\t')
	
	print 'values added to D57 SCZ line + SCZ syn and new file was created'


def plate7_SCZ_HC(norm_df, D57_SCZ_HC_file, letters_SCZ, numbers_HC, outdir_results):
	'''gets all the D57 SCZ cell lines from plate 2 with HC SYN incubated - appends to existing file and creates new file
	'''
	D57_file = pd.read_csv(D57_SCZ_HC_file, sep='\t', encoding='utf8')
	
	extracted_rows = []

	for l in letters_SCZ: 
		for n in numbers_HC:
			#select specific well letters and numbers from dataframe 
			filter_rows = norm_df.loc[(norm_df['well_letter'] == l) & (norm_df['well_number'] == n)]
			#append to a list
			extracted_rows.append(filter_rows)


	#puts everything together from list 
	df = pd.concat(extracted_rows)

	new_df=D57_file.append(df, ignore_index=True)
	#create new dataframe 
	new_df.to_csv(outdir_results+'D57_SCZline_HCsyn_3.tsv', index=False, sep='\t')
	
	print 'values added to D57 SCZ line + HC syn and new file was created'


def plate7_HC_SCZ_D105(norm_df, D105_HC_SCZ_file, letters_HC, numbers_SCZ, outdir_results):
	'''gets all the D105 HC cell lines from plate 7 with SCZ SYN incubated - appends to existing file and creates new file
	'''
	D105_file = pd.read_csv(D105_HC_SCZ_file, sep='\t', encoding='utf8')
	
	extracted_rows = []

	for l in letters_HC: 
		for n in numbers_SCZ:
			#select specific well letters and numbers from dataframe 
			filter_rows = norm_df.loc[(norm_df['well_letter'] == l) & (norm_df['well_number'] == n)]
			#append to a list
			extracted_rows.append(filter_rows)


	#puts everything together from list 
	df = pd.concat(extracted_rows)

	new_df=D105_file.append(df, ignore_index=True)
	#create new dataframe 
	new_df.to_csv(outdir_results+'D105_HCline_SCZsyn_3.tsv', index=False, sep='\t')
	
	print 'values added to D105 HC line + SCZ syn and new file was created'


def plate7_HC_HC_D105(norm_df, D105_HC_HC_file, letters_HC, numbers_HC, outdir_results):
	'''gets all the D105 HC cell lines from plate 7 with HC SYN incubated - appends to existing file and creates new file
	'''
	D105_file = pd.read_csv(D105_HC_HC_file, sep='\t', encoding='utf8')
	
	extracted_rows = []

	for l in letters_HC: 
		for n in numbers_HC:
			#select specific well letters and numbers from dataframe 
			filter_rows = norm_df.loc[(norm_df['well_letter'] == l) & (norm_df['well_number'] == n)]
			#append to a list
			extracted_rows.append(filter_rows)


	#puts everything together from list 
	df = pd.concat(extracted_rows)

	new_df=D105_file.append(df, ignore_index=True)
	#create new dataframe 
	new_df.to_csv(outdir_results+'D105_HCline_HCsyn_3.tsv', index=False, sep='\t')
	
	print 'values added to D105 HC line + HC syn and new file was created'


####MAIN####

#Split args
args = parser.parse_args()

#input files to merge all files
norm_file=args.norm_file[0]
D57_SCZ_SCZ_file=args.D57_SCZ_SCZ_file[0]
D57_SCZ_HC_file=args.D57_SCZ_HC_file[0]
D105_HC_SCZ_file=args.D105_HC_SCZ_file[0]
D105_HC_HC_file=args.D105_HC_HC_file[0]

letters_HC=args.letters_HC[0].split(',')
letters_SCZ=args.letters_SCZ[0].split(',')
numbers_SCZ = np.array(args.numbers_SCZ[0].split(','),dtype='int32')
numbers_HC = np.array(args.numbers_HC[0].split(','),dtype='int32')

outdir_results=args.outdir_results[0]

norm_df = pd.read_csv(norm_file, sep='\t', encoding='utf8')
norm_df["time_point_x"].replace({'00d00h00m': 'pre','00d00h28m':'00:00','00d00h58m':'00:30','00d01h28m':'01:00','00d01h58m':'01:30','00d02h28m':'02:00','00d02h58m':'02:30','00d03h28m':'03:00','00d03h58m':'03:30','00d04h28m':'04:00','00d04h58m':'04:30','00d05h28m':'05:00','00d05h58m':'05:30','00d06h28m':'06:00','00d07h28m':'07:00','00d08h28m':'08:00','00d09h28m':'09:00','00d10h28m':'10:00','00d11h28m':'11:00','00d12h28m':'12:00','00d13h28m':'13:00','00d14h28m':'14:00','00d15h28m':'15:00','00d16h28m':'16:00','00d17h28m':'17:00','00d18h28m':'18:00','00d19h28m':'19:00','00d20h28m':'20:00','00d21h28m':'21:00','00d22h28m':'22:00','00d23h28m':'23:00','01d00h28m':'24:00'}, inplace=True)

#add plate 7 cell lines two the files created from plate 1
plate7_SCZ_SCZ(norm_df, D57_SCZ_SCZ_file, letters_SCZ, numbers_SCZ, outdir_results)
plate7_SCZ_HC(norm_df, D57_SCZ_HC_file, letters_SCZ, numbers_HC, outdir_results)
plate7_HC_SCZ_D105(norm_df, D105_HC_SCZ_file, letters_HC, numbers_SCZ, outdir_results)
plate7_HC_HC_D105(norm_df, D105_HC_HC_file, letters_HC, numbers_HC, outdir_results)




