#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###Merge files 

import os
import glob
import pandas as pd
import sys
import pdb
import argparse

###Arguments for argparse module###
parser = argparse.ArgumentParser(description = '''A program that merges all colfuency files from Plates 1, 2, 3, 4, 6, 7, 8''')

parser.add_argument('--plate_dir', nargs=1, type= str, default=sys.stdin, help = 'path to directory with results per plate')
parser.add_argument('--prefix', nargs=1, type= str, default=sys.stdin, help = 'Plate prefix')
parser.add_argument('--letters', nargs=1, type= str, default=sys.stdin, help = 'Letter separated by comma as str: B,C,D,E,F,G')
parser.add_argument('--well_numbers', nargs=1, type= str, default=sys.stdin, help = 'Well numbers separated by comma as str: 2,3,8,9')
parser.add_argument('--picture_numbers', nargs=1, type= str, default=sys.stdin, help = 'Picture numbers separated by comma as str: 1,2,3,4,5')
parser.add_argument('--outdir', nargs=1, type= str, default=sys.stdin, help = 'Path to output directory')


####FUNCTIONS####
def merge_plates(plate_dir, prefix, letters, well_numbers, picture_numbers, outdir):
    '''Merge plate results into one file
    '''
    well_ids = []
    extracted_l = []
    extracted_n1 = []
    extracted_n2 = []
    time_point = []
    percent_areas = []
    for letter in letters:
        for n1 in well_numbers:
            for n2 in picture_numbers:
                well_pic_name=letter+n1+'_'+n2
                #Get all matching well_pic_name
                all_well_pics = glob.glob(plate_dir+prefix+"_"+well_pic_name+"*")
                #Go through all found matches

                for entry in all_well_pics:
                    #Open the file
                    with open(entry) as file:
                        #Go through each line in the file
                        lc = 0 #line count
                        for line in file:
                            lc+=1
                            if lc==2:
                                line = line.rstrip() #Remove lagging newlines
                                line = line.split('\t') #Split on tab
                                time_point.append(line[0].split('_')[-1].split('-')[0])
                                well_ids.append(line[0]) #Save well id
                                extracted_l.append(letter)
                                extracted_n1.append(n1)
                                extracted_n2.append(n2)
                                percent_areas.append(float(line[-1])) #Save as float (decimal number)
                
    #Create dataframe
    results = pd.DataFrame()
    results['well_id']=well_ids
    results['well_letter']=extracted_l
    results['well_number']=extracted_n1
    results['picture']=extracted_n2
    results['time_point']=time_point
    results['percent_area']=percent_areas
    #pdb.set_trace()
    results.to_csv(outdir+'confluency_merged.tsv', index=False, sep='\t')

    print 'Confluency files merged'


#####MAIN#####
#Split args
args = parser.parse_args()
#input files to merge all files
plate_dir = args.plate_dir[0]
prefix = args.prefix[0]
letters = args.letters[0].split(',')
well_numbers = args.well_numbers[0].split(',')
picture_numbers = args.picture_numbers[0].split(',')
outdir= args.outdir[0]

#Merge
merge_plates(plate_dir, prefix, letters, well_numbers, picture_numbers, outdir)
