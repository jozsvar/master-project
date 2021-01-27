#!/bin/bash -l

###RUNSCRIPT###

BASE=/Volumes/Documents/Lab_work/KI_Carl_Sellgren/Incucyte_Analys/


####Create new dataframes with different conditions from Plate 1####
NORM_FILE1=$BASE/Plate1_Merged/normalized_averaged.tsv
LETTERS_SCZ='B,C,D,E'
LETTERS_HC='F,G'
NUMBERS_SCZ='2,3'
NUMBERS_HC='8,9'
OUTDIR_RESULTS=$BASE/D57_D105_norm_avr_files/
mkdir $OUTDIR_RESULTS

#Run script create files D57
python ./fetch_D57_data.py --norm_file $NORM_FILE1 --letters_SCZ $LETTERS_SCZ --letters_HC $LETTERS_HC --numbers_SCZ $NUMBERS_SCZ --numbers_HC $NUMBERS_HC --outdir_results $OUTDIR_RESULTS
wait
echo Files from Plate 1 created


####Appends the data from Plate 2 to dataframes created from Plate 1####
NORM_FILE2=$BASE/Plate2_Merged/normalized_averaged.tsv
D57_SCZ_SCZ=$BASE/D57_D105_norm_avr_files/D57_SCZline_SCZsyn.tsv
D57_SCZ_HC=$BASE/D57_D105_norm_avr_files/D57_SCZline_HCsyn.tsv
D57_HC_SCZ=$BASE/D57_D105_norm_avr_files/D57_HCline_SCZsyn.tsv
D57_HC_HC=$BASE/D57_D105_norm_avr_files/D57_HCline_HCsyn.tsv

LETTERS_HC_2='B,C,D,E'
LETTERS_SCZ_2='F,G'

#Run script to add data from plate 2 to plate 1
python ./assign_data_plate2.py --norm_file $NORM_FILE2 --D57_SCZ_SCZ_file $D57_SCZ_SCZ --D57_SCZ_HC_file $D57_SCZ_HC --D57_HC_SCZ_file $D57_HC_SCZ --D57_HC_HC_file $D57_HC_HC --letters_HC_2 $LETTERS_HC_2 --letters_SCZ_2 $LETTERS_SCZ_2 --numbers_SCZ $NUMBERS_SCZ --numbers_HC $NUMBERS_HC --outdir_results $OUTDIR_RESULTS

wait
echo Data from Plate 2 was added to Plate 1

####Create new dataframes with different conditions from Plate 4####
NORM_FILE4=$BASE/Plate4_Merged/normalized_averaged.tsv
LETTERS_SCZ_4='B'
LETTERS_HC_4='C,D,E,G'

OUTDIR_RESULTS=$BASE/D57_D105_norm_avr_files/

#Run script create files D105
python ./fetch_D105_data.py --norm_file $NORM_FILE4 --letters_SCZ $LETTERS_SCZ_4 --letters_HC $LETTERS_HC_4 --numbers_SCZ $NUMBERS_SCZ --numbers_HC $NUMBERS_HC --outdir_results $OUTDIR_RESULTS
wait
echo Files from Plate 4 created


####Appends the data from Plate 3 to dataframes created from Plate 1####
NORM_FILE3=$BASE/Plate3_Merged/normalized_averaged.tsv
D57_SCZ_SCZ1=$BASE/D57_D105_norm_avr_files/D57_SCZline_SCZsyn_1.tsv
D57_SCZ_HC1=$BASE/D57_D105_norm_avr_files/D57_SCZline_HCsyn_1.tsv
D105_HC_SCZ=$BASE/D57_D105_norm_avr_files/D105_HCline_SCZsyn.tsv
D105_HC_HC=$BASE/D57_D105_norm_avr_files/D105_HCline_HCsyn.tsv

LETTERS_SCZ_3='B,C'
LETTERS_HC_3='E,G'

#Run script to add data from plate 3 to plate 1 and plate 4
python ./assign_data_plate3.py --norm_file $NORM_FILE3 --D57_SCZ_SCZ_file $D57_SCZ_SCZ1 --D57_SCZ_HC_file $D57_SCZ_HC1 --D105_HC_SCZ_file $D105_HC_SCZ --D105_HC_HC_file $D105_HC_HC --letters_SCZ $LETTERS_SCZ_3 --letters_HC1 $LETTERS_HC_3 --numbers_SCZ $NUMBERS_SCZ --numbers_HC $NUMBERS_HC --outdir_results $OUTDIR_RESULTS
wait
echo Data from Plate 3 was added to Plate 1 and Plate 4


####Appends the data from Plate 6 to dataframes created from Plate 4####
NORM_FILE6=$BASE/Plate6_Merged/normalized_averaged.tsv
D105_SCZ_SCZ=$BASE/D57_D105_norm_avr_files/D105_SCZline_SCZsyn.tsv
D105_SCZ_HC=$BASE/D57_D105_norm_avr_files/D105_SCZline_HCsyn.tsv
D105_HC_SCZ1=$BASE/D57_D105_norm_avr_files/D105_HCline_SCZsyn_1.tsv
D105_HC_HC1=$BASE/D57_D105_norm_avr_files/D105_HCline_HCsyn_1.tsv

LETTERS_HC6='E'
LETTERS_SCZ6='B,C,D,F,G'
LETTERS_SCZ_dead='B,C,D'
LETTERS_SCZ_g='F,G'
NUMBERS_HCn='6,7'

#Run script to add data from plate 6 to plate 4
python ./assign_data_plate6.py --norm_file $NORM_FILE6 --D105_SCZ_SCZ_file $D105_SCZ_SCZ --D105_SCZ_HC_file $D105_SCZ_HC --D105_HC_SCZ_file $D105_HC_SCZ --D105_HC_HC_file $D105_HC_HC --letters_HC $LETTERS_HC6 --letters_SCZ1 $LETTERS_SCZ_dead --letters_SCZ2 $LETTERS_SCZ_g --letters_SCZ3 $LETTERS_SCZ6 --numbers_SCZ $NUMBERS_SCZ --numbers_HC $NUMBERS_HCn --outdir_results $OUTDIR_RESULTS
wait
echo Data from Plate 6 was added to Plate 4

####Appends the data from Plate 7 to dataframes created from Plate 1 and Plate 4####
NORM_FILE7=$BASE/Plate7_Merged/normalized_averaged.tsv
D57_SCZ_SCZ2=$BASE/D57_D105_norm_avr_files/D57_SCZline_SCZsyn_2.tsv
D57_SCZ_HC2=$BASE/D57_D105_norm_avr_files/D57_SCZline_HCsyn_2.tsv
D105_HC_SCZ2=$BASE/D57_D105_norm_avr_files/D105_HCline_SCZsyn_2.tsv
D105_HC_HC2=$BASE/D57_D105_norm_avr_files/D105_HCline_HCsyn_2.tsv

LETTERS_SCZ7='B,C,D'
LETTERS_HC7='E'

#Run script to add data from plate 7 to plate 1 and 4
python ./assign_data_plate7.py --norm_file $NORM_FILE7 --D57_SCZ_SCZ_file $D57_SCZ_SCZ2 --D57_SCZ_HC_file $D57_SCZ_HC2 --D105_HC_SCZ_file $D105_HC_SCZ2 --D105_HC_HC_file $D105_HC_HC2 --letters_SCZ $LETTERS_SCZ7 --letters_HC $LETTERS_HC7 --numbers_SCZ $NUMBERS_SCZ --numbers_HC $NUMBERS_HCn --outdir_results $OUTDIR_RESULTS
wait
echo Data from Plate 7 was added to Plate 1 and Plate 4


####Appends the data from Plate 8 to dataframes created from Plate 4####
NORM_FILE8=$BASE/Plate8_Merged/normalized_averaged.tsv
D105_SCZ_SCZ_d=$BASE/D57_D105_norm_avr_files/D105_SCZline_SCZsyn_dead.tsv
D105_SCZ_HC1=$BASE/D57_D105_norm_avr_files/D105_SCZline_HCsyn_1.tsv

LETTERS_SCZ8='B,C'

#Run script to add data from plate 8 to Plate 4 and to the dead file 
python ./assign_data_plate8.py --norm_file $NORM_FILE8 --D105_SCZ_SCZ_dead_file $D105_SCZ_SCZ_d --D105_SCZ_HC_file $D105_SCZ_HC1 --letters_SCZ $LETTERS_SCZ8 --numbers_SCZ $NUMBERS_SCZ --numbers_HC $NUMBERS_HCn --outdir_results $OUTDIR_RESULTS
wait
echo Data from Plate 8 was added to Plate 4