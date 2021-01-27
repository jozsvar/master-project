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

parser.add_argument('--norm_file', nargs=1, type= str, default=sys.stdin, help = 'Path to normalized plate 6 file')
parser.add_argument('--D105_SCZ_SCZ_file', nargs=1, type= str, default=sys.stdin, help = 'Path to: D105_SCZline_SCZsyn.tsv')
parser.add_argument('--D105_SCZ_HC_file', nargs=1, type= str, default=sys.stdin, help = 'Path to: D105_SCZline_HCsyn.tsv')
parser.add_argument('--D105_HC_SCZ_file', nargs=1, type= str, default=sys.stdin, help = 'Path to: D105_HCline_SCZsyn.tsv_1')
parser.add_argument('--D105_HC_HC_file', nargs=1, type= str, default=sys.stdin, help = 'Path to: D105_HCline_HCsyn.tsv_1')

parser.add_argument('--letters_HC', nargs=1, type= str, default=sys.stdin, help = 'Letters for HC lines separated by comma as str: E')
parser.add_argument('--letters_SCZ1', nargs=1, type= str, default=sys.stdin, help = 'Letters for SCZ lines separated by comma as str: B,C,D')
parser.add_argument('--letters_SCZ2', nargs=1, type= str, default=sys.stdin, help = 'Letters for SCZ lines separated by comma as str: F,G')
parser.add_argument('--letters_SCZ3', nargs=1, type= str, default=sys.stdin, help = 'Letters for SCZ lines separated by comma as str: B,C,D,F,G')
parser.add_argument('--numbers_SCZ', nargs=1, type= str, default=sys.stdin, help = 'Well numbers for SCZ SYN separated by comma as int: 2,3')
parser.add_argument('--numbers_HC', nargs=1, type= str, default=sys.stdin, help = 'Well numbers for HC SYN separated by comma as int: 6,7')

parser.add_argument('--outdir_results', nargs=1, type= str, default=sys.stdin, help = 'Path to output directory to results folder')


###FUNCTION####


def plate6_SCZ_SCZ(norm_df, D105_SCZ_SCZ_file, letters_SCZ2, numbers_SCZ, outdir_results):
	'''gets all the D105 SCZ cell lines from plate 6 with SCZ SYN incubated - appends to existing file and creates new file
	'''
	D105_file = pd.read_csv(D105_SCZ_SCZ_file, sep='\t', encoding='utf8')
	
	extracted_rows = []

	for l in letters_SCZ2: 
		for n in numbers_SCZ:
			#select specific well letters and numbers from dataframe 
			filter_rows = norm_df.loc[(norm_df['well_letter'] == l) & (norm_df['well_number'] == n)]
			#append to a list
			extracted_rows.append(filter_rows)


	#puts everything together from list 
	df = pd.concat(extracted_rows)

	new_df=D105_file.append(df, ignore_index=True)
	#create new dataframe 
	new_df.to_csv(outdir_results+'D105_SCZline_SCZsyn_1.tsv', index=False, sep='\t')
	
	print 'values added to D105 SCZ line + SCZ syn and new file was created'


def plate6_SCZ_SCZ_dead(norm_df, D105_SCZ_SCZ_file, letters_SCZ1, numbers_SCZ, outdir_results):
	'''gets all the D105 SCZ cell lines from plate 6 with SCZ SYN incubated and cells died - creates a new file for those 
	'''
	D105_file = pd.read_csv(D105_SCZ_SCZ_file, sep='\t', encoding='utf8')
	
	extracted_rows = []

	for l in letters_SCZ1: 
		for n in numbers_SCZ:
			#select specific well letters and numbers from dataframe 
			filter_rows = norm_df.loc[(norm_df['well_letter'] == l) & (norm_df['well_number'] == n)]
			#append to a list
			extracted_rows.append(filter_rows)


	#puts everything together from list 
	df = pd.concat(extracted_rows)

	new_df=D105_file.append(df, ignore_index=True)
	#create new dataframe 
	new_df.to_csv(outdir_results+'D105_SCZline_SCZsyn_dead.tsv', index=False, sep='\t')
	
	print 'values added to D105 SCZ line + SCZ syn and new file was created'


def plate6_SCZ_HC(norm_df, D105_SCZ_HC_file, letters_SCZ3, numbers_HC, outdir_results):
	'''gets all the D105 SCZ cell lines from plate 6 with HC SYN incubated - appends to existing file and creates new file
	'''
	D105_file = pd.read_csv(D105_SCZ_HC_file, sep='\t', encoding='utf8')
	
	extracted_rows = []

	for l in letters_SCZ3: 
		for n in numbers_HC:
			#select specific well letters and numbers from dataframe 
			filter_rows = norm_df.loc[(norm_df['well_letter'] == l) & (norm_df['well_number'] == n)]
			#append to a list
			extracted_rows.append(filter_rows)


	#puts everything together from list 
	df = pd.concat(extracted_rows)

	new_df=D105_file.append(df, ignore_index=True)
	#create new dataframe 
	new_df.to_csv(outdir_results+'D105_SCZline_HCsyn_1.tsv', index=False, sep='\t')
	
	print 'values added to D105 SCZ line + HC syn and new file was created'


def plate6_HC_SCZ(norm_df, D105_HC_SCZ_file, letters_HC, numbers_SCZ, outdir_results):
	'''gets all the D105 HC cell lines from plate 6 with SCZ SYN incubated - appends to existing file and creates new file
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
	new_df.to_csv(outdir_results+'D105_HCline_SCZsyn_2.tsv', index=False, sep='\t')
	
	print 'values added to D105 HC line + SCZ syn and new file was created'



def plate6_HC_HC(norm_df, D105_HC_HC_file, letters_HC, numbers_HC, outdir_results):
	'''gets all the D105 HC cell lines from plate 6 with HC SYN incubated - appends to existing file and creates new file
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
	new_df.to_csv(outdir_results+'D105_HCline_HCsyn_2.tsv', index=False, sep='\t')
	
	print 'values added to D105 HC line + HC syn and new file was created'


####MAIN####

#Split args
args = parser.parse_args()

#input files to merge all files
norm_file=args.norm_file[0]
D105_SCZ_SCZ_file=args.D105_SCZ_SCZ_file[0]
D105_SCZ_HC_file=args.D105_SCZ_HC_file[0]
D105_HC_SCZ_file=args.D105_HC_SCZ_file[0]
D105_HC_HC_file=args.D105_HC_HC_file[0]

letters_HC=args.letters_HC[0].split(',')
letters_SCZ1=args.letters_SCZ1[0].split(',')
letters_SCZ2=args.letters_SCZ2[0].split(',')
letters_SCZ3=args.letters_SCZ3[0].split(',')
numbers_SCZ = np.array(args.numbers_SCZ[0].split(','),dtype='int32')
numbers_HC = np.array(args.numbers_HC[0].split(','),dtype='int32')

outdir_results=args.outdir_results[0]

norm_df = pd.read_csv(norm_file, sep='\t', encoding='utf8')
norm_df["time_point_x"].replace({'00d00h00m': 'pre','00d00h40m':'00:00','00d01h10m':'00:30','00d01h40m':'01:00','00d02h10m':'01:30','00d02h40m':'02:00','00d03h10m':'02:30','00d03h40m':'03:00','00d04h10m':'03:30','00d04h40m':'04:00','00d05h10m':'04:30','00d05h40m':'05:00','00d06h10m':'05:30','00d06h40m':'06:00','00d07h40m':'07:00','00d08h40m':'08:00','00d09h40m':'09:00','00d10h40m':'10:00','00d11h40m':'11:00','00d12h40m':'12:00','00d13h40m':'13:00','00d14h40m':'14:00','00d15h40m':'15:00','00d16h40m':'16:00','00d17h40m':'17:00','00d18h40m':'18:00','00d19h40m':'19:00','00d20h40m':'20:00','00d21h40m':'21:00','00d22h40m':'22:00','00d23h40m':'23:00','01d00h40m':'24:00'}, inplace=True)

#add plate 6 cell lines two the files created from plate 4
plate6_SCZ_SCZ(norm_df, D105_SCZ_SCZ_file, letters_SCZ2, numbers_SCZ, outdir_results)
plate6_SCZ_SCZ_dead(norm_df, D105_SCZ_SCZ_file, letters_SCZ1, numbers_SCZ, outdir_results)
plate6_SCZ_HC(norm_df, D105_SCZ_HC_file, letters_SCZ3, numbers_HC, outdir_results)
plate6_HC_SCZ(norm_df, D105_HC_SCZ_file, letters_HC, numbers_SCZ, outdir_results)
plate6_HC_HC(norm_df, D105_HC_HC_file, letters_HC, numbers_HC, outdir_results)





