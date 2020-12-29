#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import glob
import pandas as pd
import numpy as np
import pdb
import re as re
import argparse
import sys

###Arguments for argparse module###
parser = argparse.ArgumentParser(description = '''A program that normalizes the percent areas''')

parser.add_argument('--confluence_file', nargs=1, type= str, default=sys.stdin, help = 'Path to merged confluency file')
parser.add_argument('--particle_file', nargs=1, type= str, default=sys.stdin, help = 'Path to merged partcicle file')
parser.add_argument('--outdir', nargs=1, type= str, default=sys.stdin, help = 'directory to output file')

### FUNCTION ###

def norm_pct_area(confluence_file, particle_file, outdir):
	'''Normalizing function: merges dataframes and normalized percent areas 
    '''
    
	conf_df = pd.read_csv(confluence_file, sep='\t', encoding='utf8')
	part_df = pd.read_csv(particle_file, sep='\t', encoding='utf8')

	#merges the particle file and the confluency file on well letter, well number and picture 
	matched_df = pd.merge(part_df, conf_df,  how='left', on=[u'well_letter', u'well_number', u'picture'])
	#Get normalized area: divides %Area_X = Particle Area by %Area_Y = Confluency Area of T0
	norm_area = np.array(matched_df[u'percent_area_x']/matched_df[u'percent_area_y'])
	#Assign a new column
	matched_df['Normalized_area'] = norm_area 
	#Save
	matched_df.to_csv(outdir+'normalized.tsv', index=False, sep='\t')


### MAIN ###
#Split args
args = parser.parse_args()

#input files to merge all files
confluence_file = args.confluence_file[0]
particle_file = args.particle_file[0]
outdir = args.outdir[0]

#Merge and normalize
norm_pct_area(confluence_file, particle_file, outdir)
