#!/bin/bash -l

###RUNSCRIPT###

BASE=/Volumes/Documents/Lab_work/KI_Carl_Sellgren/Incucyte_Analys/


#Plate1: average cell lines/well
FILE1=$BASE/Plate1_Merged/normalized.tsv
LETTER1='B,C,D,E,F,G'
NUMBERS1_1='2,3'
NUMBERS2_1='8,9'
PLATE1='Plate_1'
OUTDIR1=$BASE/Plate1_Merged/

#Run script
python ./average_same_line.py --file $FILE1 --letter $LETTER1 --numbers1 $NUMBERS1_1 --numbers2 $NUMBERS2_1 --plate $PLATE1 --outdir $OUTDIR1
wait
echo Cell lines averaged and new file created of plate 1


#Plate2: average cell lines/well
FILE2=$BASE/Plate2_Merged/normalized.tsv
PLATE2='Plate_2'
OUTDIR2=$BASE/Plate2_Merged/

#Run script
python ./average_same_line.py --file $FILE2 --letter $LETTER1 --numbers1 $NUMBERS1_1 --numbers2 $NUMBERS2_1 --plate $PLATE2 --outdir $OUTDIR2
wait
echo Cell lines averaged and new file created of plate 2


#Plate3: average cell lines/well
FILE3=$BASE/Plate3_Merged/normalized.tsv
PLATE3='Plate_3'
LETTER3='B,C,E,F,G'
OUTDIR3=$BASE/Plate3_Merged/

#Run script
python ./average_same_line.py --file $FILE3 --letter $LETTER3 --numbers1 $NUMBERS1_1 --numbers2 $NUMBERS2_1 --plate $PLATE3 --outdir $OUTDIR3
wait
echo Cell lines averaged and new file created of plate 3


#Plate4: average cell lines/well
FILE4=$BASE/Plate4_Merged/normalized.tsv
PLATE4='Plate_4'
LETTER4='B,C,D,E,G'
OUTDIR4=$BASE/Plate4_Merged/

#Run script
python ./average_same_line.py --file $FILE4 --letter $LETTER4 --numbers1 $NUMBERS1_1 --numbers2 $NUMBERS2_1 --plate $PLATE4 --outdir $OUTDIR4
wait
echo Cell lines averaged and new file created of plate 4


#Plate6: average cell lines/well
FILE6=$BASE/Plate6_Merged/normalized.tsv
PLATE6='Plate_6'
NUMBERS2_6='6,7'
OUTDIR6=$BASE/Plate6_Merged/


#Run script
python ./average_same_line.py --file $FILE6 --letter $LETTER1 --numbers1 $NUMBERS1_1 --numbers2 $NUMBERS2_6 --plate $PLATE6 --outdir $OUTDIR6
wait
echo Cell lines averaged and new file created of plate 6


#Plate7: average cell lines/well
FILE7=$BASE/Plate7_Merged/normalized.tsv
PLATE7='Plate_7'
LETTER7='B,C,D,E'
OUTDIR7=$BASE/Plate7_Merged/


#Run script
python ./average_same_line.py --file $FILE7 --letter $LETTER7 --numbers1 $NUMBERS1_1 --numbers2 $NUMBERS2_6 --plate $PLATE7 --outdir $OUTDIR7
wait
echo Cell lines averaged and new file created of plate 7


#Plate8: average cell lines/well
FILE8=$BASE/Plate8_Merged/normalized.tsv
PLATE8='Plate_8'
LETTER8='B,C'
OUTDIR8=$BASE/Plate8_Merged/


#Run script
python ./average_same_line.py --file $FILE8 --letter $LETTER8 --numbers1 $NUMBERS1_1 --numbers2 $NUMBERS2_6 --plate $PLATE8 --outdir $OUTDIR8
wait
echo Cell lines averaged and new file created of plate 8






