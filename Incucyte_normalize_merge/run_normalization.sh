#!/bin/bash -l

###RUNSCRIPT###

BASE=/Volumes/Documents/Lab_work/KI_Carl_Sellgren/Incucyte_Analys/


###NORMALIZE DATA###

#Plate 1
CONF_FILE1=$BASE/Plate1_Merged/confluency_merged.tsv
PART_FILE1=$BASE/Plate1_Merged/particle_merged.tsv
NORM_OUTDIR1=$BASE/Plate1_Merged/

#Run script normalization of plate 1 
python ./Normalize_data.py --confluence_file $CONF_FILE1 --particle_file $PART_FILE1 --outdir $NORM_OUTDIR1
wait
echo Plate 1: dataframes merged and normalized 


#Plate 2
CONF_FILE2=$BASE/Plate2_Merged/confluency_merged.tsv
PART_FILE2=$BASE/Plate2_Merged/particle_merged.tsv
NORM_OUTDIR2=$BASE/Plate2_Merged/

#Run script normalization of plate 2 
python ./Normalize_data.py --confluence_file $CONF_FILE2 --particle_file $PART_FILE2 --outdir $NORM_OUTDIR2
wait
echo Plate 2: dataframes merged and normalized 


#Plate 3
CONF_FILE3=$BASE/Plate3_Merged/confluency_merged.tsv
PART_FILE3=$BASE/Plate3_Merged/particle_merged.tsv
NORM_OUTDIR3=$BASE/Plate3_Merged/

#Run script normalization of plate 3 
python ./Normalize_data.py --confluence_file $CONF_FILE3 --particle_file $PART_FILE3 --outdir $NORM_OUTDIR3
wait
echo Plate 3: dataframes merged and normalized 


#Plate 4
CONF_FILE4=$BASE/Plate4_Merged/confluency_merged.tsv
PART_FILE4=$BASE/Plate4_Merged/particle_merged.tsv
NORM_OUTDIR4=$BASE/Plate4_Merged/

#Run script normalization of plate 4 
python ./Normalize_data.py --confluence_file $CONF_FILE4 --particle_file $PART_FILE4 --outdir $NORM_OUTDIR4
wait
echo Plate 4: dataframes merged and normalized 


#Plate 6
CONF_FILE6=$BASE/Plate6_Merged/confluency_merged.tsv
PART_FILE6=$BASE/Plate6_Merged/particle_merged.tsv
NORM_OUTDIR6=$BASE/Plate6_Merged/

#Run script normalization of plate 6
python ./Normalize_data.py --confluence_file $CONF_FILE6 --particle_file $PART_FILE6 --outdir $NORM_OUTDIR6
wait
echo Plate 6: dataframes merged and normalized 


#Plate 7
CONF_FILE7=$BASE/Plate7_Merged/confluency_merged.tsv
PART_FILE7=$BASE/Plate7_Merged/particle_merged.tsv
NORM_OUTDIR7=$BASE/Plate7_Merged/

#Run script normalization of plate 7
python ./Normalize_data.py --confluence_file $CONF_FILE7 --particle_file $PART_FILE7 --outdir $NORM_OUTDIR7
wait
echo Plate 7: dataframes merged and normalized 


#Plate 8
CONF_FILE8=$BASE/Plate8_Merged/confluency_merged.tsv
PART_FILE8=$BASE/Plate8_Merged/particle_merged.tsv
NORM_OUTDIR8=$BASE/Plate8_Merged/

#Run script normalization of plate 7
python ./Normalize_data.py --confluence_file $CONF_FILE8 --particle_file $PART_FILE8 --outdir $NORM_OUTDIR8
wait
echo Plate 8: dataframes merged and normalized 