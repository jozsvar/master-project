#!/bin/bash -l

###RUNSCRIPT###

BASE=/Volumes/Documents/Lab_work/KI_Carl_Sellgren/Incucyte_Analys/

###MERGE CONFLUENCY FILES###

###PLATE 1 CONFLUENCY###

#INPUT PLATE 1 CONFLUENCY
PLATE_DIR1_1=$BASE/Cell_Area_T0_Plate1/

#RUN SKRIPT PLATE 1 CONFLUENCY
python ./merge_confluency_files.py --plate_dir $PLATE_DIR1_1 --prefix $PREFIX1 --letters $LETTERS1 --well_numbers $WELL_NUMBERS1 --picture_numbers $PICTURE_NUMBERS1 --outdir $OUTDIR1
wait
echo Plate 1 confluency merged


###PLATE 2 CONFLUENCY###

#INPUT PLATE 2 CONFLUENCY
PLATE_DIR2_1=$BASE/Cell_Area_T0_Plate2/

#RUN SKRIPT PLATE 2 CONFLUENCY
python ./merge_confluency_files.py --plate_dir $PLATE_DIR2_1 --prefix $PREFIX2 --letters $LETTERS2 --well_numbers $WELL_NUMBERS2 --picture_numbers $PICTURE_NUMBERS2 --outdir $OUTDIR2
wait
echo Plate 2 confluency merged


###PLATE 3 CONFLUENCY###

#INPUT PLATE 3 CONFLUENCY
PLATE_DIR3_1=$BASE/Cell_Area_T0_Plate3/

#RUN SKRIPT PLATE 3 CONFLUENCY
python ./merge_confluency_files.py --plate_dir $PLATE_DIR3_1 --prefix $PREFIX3 --letters $LETTERS3 --well_numbers $WELL_NUMBERS3 --picture_numbers $PICTURE_NUMBERS3 --outdir $OUTDIR3
wait
echo Plate 3 confluency merged


###PLATE 4 CONFLUENCY###

#INPUT PLATE 4 CONFLUENCY
PLATE_DIR4_1=$BASE/Cell_Area_T0_Plate4/

#RUN SKRIPT PLATE 4 CONFLUENCY
python ./merge_confluency_files.py --plate_dir $PLATE_DIR4_1 --prefix $PREFIX4 --letters $LETTERS4 --well_numbers $WELL_NUMBERS4 --picture_numbers $PICTURE_NUMBERS4 --outdir $OUTDIR4
wait
echo Plate 4 confluency merged


###PLATE 6 CONFLUENCY###

#INPUT PLATE 6 CONFLUENCY
PLATE_DIR6_1=$BASE/Cell_Area_T0_Plate6/

#RUN SKRIPT PLATE 6 CONFLUENCY
python ./merge_confluency_files.py --plate_dir $PLATE_DIR6_1 --prefix $PREFIX6 --letters $LETTERS6 --well_numbers $WELL_NUMBERS6 --picture_numbers $PICTURE_NUMBERS6 --outdir $OUTDIR6
wait
echo Plate 6 confluency merged


###PLATE 7 CONFLUENCY###

#INPUT PLATE 7 CONFLUENCY
PLATE_DIR7_1=$BASE/Cell_Area_T0_Plate7/

#RUN SKRIPT PLATE 7 CONFLUENCY
python ./merge_confluency_files.py --plate_dir $PLATE_DIR7_1 --prefix $PREFIX7 --letters $LETTERS7 --well_numbers $WELL_NUMBERS7 --picture_numbers $PICTURE_NUMBERS7 --outdir $OUTDIR7
wait
echo Plate 7 confluency merged


###PLATE 8 CONFLUENCY###

#INPUT PLATE 8 CONFLUENCY
PLATE_DIR8_1=$BASE/Cell_Area_T0_Plate8/

#RUN SKRIPT PLATE 8 CONFLUENCY
python ./merge_confluency_files.py --plate_dir $PLATE_DIR8_1 --prefix $PREFIX8 --letters $LETTERS8 --well_numbers $WELL_NUMBERS8 --picture_numbers $PICTURE_NUMBERS8 --outdir $OUTDIR8
wait
echo Plate 8 confluency merged