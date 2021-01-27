#!/bin/bash -l

###RUNSCRIPT###

BASE=/Volumes/Documents/Lab_work/KI_Carl_Sellgren/Incucyte_Analys/


###MERGE PARTICLE FILES###

###PLATE 1 PARTICLES###

#INPUT PLATE 1
PLATE_DIR1=$BASE/Particle_Numbers_Plate1/
PREFIX1='whatever'
LETTERS1='B,C,D,E,F,G'
WELL_NUMBERS1='2,3,8,9'
PICTURE_NUMBERS1='1,2,3,4,5'

#OUTPUT DIRECTORY PLATE 1
OUTDIR1=$BASE/Plate1_Merged/
mkdir $OUTDIR1

#RUN SKRIPT PLATE 1
python ./merge_particle_files.py --plate_dir $PLATE_DIR1 --prefix $PREFIX1 --letters $LETTERS1 --well_numbers $WELL_NUMBERS1 --picture_numbers $PICTURE_NUMBERS1 --outdir $OUTDIR1
wait
echo Plate 1 particles merged

###PLATE 2 PARTICLES###

#INPUT PLATE 2
PLATE_DIR2=$BASE/Particle_Numbers_Plate2/
PREFIX2='PhagoAssay_Plate2_20201014'
LETTERS2='B,C,D,E,F,G'
WELL_NUMBERS2='2,3,8,9'
PICTURE_NUMBERS2='1,2,3,4,5'

#OUTPUT DIRECTORY PLATE 2
OUTDIR2=$BASE/Plate2_Merged/
mkdir $OUTDIR2

#RUN SKRIPT PLATE 2
python ./merge_particle_files.py --plate_dir $PLATE_DIR2 --prefix $PREFIX2 --letters $LETTERS2 --well_numbers $WELL_NUMBERS2 --picture_numbers $PICTURE_NUMBERS2 --outdir $OUTDIR2
wait
echo Plate 2 particles merged


###PLATE 3 PARTICLES###

#INPUT PLATE 3
PLATE_DIR3=$BASE/Particle_Numbers_Plate3/
PREFIX3='PhagoAssay_Plate3_20201021'
LETTERS3='B,C,E,F,G'
WELL_NUMBERS3='2,3,8,9'
PICTURE_NUMBERS3='1,2,3,4,5'

#OUTPUT DIRECTORY PLATE 3
OUTDIR3=$BASE/Plate3_Merged/
mkdir $OUTDIR3

#RUN SKRIPT PLATE 3
python ./merge_particle_files.py --plate_dir $PLATE_DIR3 --prefix $PREFIX3 --letters $LETTERS3 --well_numbers $WELL_NUMBERS3 --picture_numbers $PICTURE_NUMBERS3 --outdir $OUTDIR3
wait
echo Plate 3 particles merged


###PLATE 4 PARTICLES###

#INPUT PLATE 4
PLATE_DIR4=$BASE/Particle_Numbers_Plate4/
PREFIX4='PhagoAssay_Plate4_20201022'
LETTERS4='B,C,D,E,G'
WELL_NUMBERS4='2,3,8,9'
PICTURE_NUMBERS4='1,2,3,4,5'

#OUTPUT DIRECTORY PLATE 4
OUTDIR4=$BASE/Plate4_Merged/
mkdir $OUTDIR4

#RUN SKRIPT PLATE 4
python ./merge_particle_files.py --plate_dir $PLATE_DIR4 --prefix $PREFIX4 --letters $LETTERS4 --well_numbers $WELL_NUMBERS4 --picture_numbers $PICTURE_NUMBERS4 --outdir $OUTDIR4
wait
echo Plate 4 particles merged


###PLATE 6 PARTICLES###

#INPUT PLATE 6
PLATE_DIR6=$BASE/Particle_Numbers_Plate6/
PREFIX6='PhagoAssay_Plate6_20201104'
LETTERS6='B,C,D,E,F,G'
WELL_NUMBERS6='2,3,6,7'
PICTURE_NUMBERS6='1,2,3,4,5'

#OUTPUT DIRECTORY PLATE 6
OUTDIR6=$BASE/Plate6_Merged/
mkdir $OUTDIR6

#RUN SKRIPT PLATE 6
python ./merge_particle_files.py --plate_dir $PLATE_DIR6 --prefix $PREFIX6 --letters $LETTERS6 --well_numbers $WELL_NUMBERS6 --picture_numbers $PICTURE_NUMBERS6 --outdir $OUTDIR6
wait
echo Plate 6 particles merged


###PLATE 7 PARTICLES###

#INPUT PLATE 7
PLATE_DIR7=$BASE/Particle_Numbers_Plate7/
PREFIX7='PhagoAssay_Plate7_20201104'
LETTERS7='B,C,D,E'
WELL_NUMBERS7='2,3,6,7'
PICTURE_NUMBERS7='1,2,3,4,5'

#OUTPUT DIRECTORY PLATE 7
OUTDIR7=$BASE/Plate7_Merged/
mkdir $OUTDIR7

#RUN SKRIPT PLATE 7
python ./merge_particle_files.py --plate_dir $PLATE_DIR7 --prefix $PREFIX7 --letters $LETTERS7 --well_numbers $WELL_NUMBERS7 --picture_numbers $PICTURE_NUMBERS7 --outdir $OUTDIR7
wait
echo Plate 7 particles merged


###PLATE 8 PARTICLES###

#INPUT PLATE 8
PLATE_DIR8=$BASE/Particle_Numbers_Plate8/
PREFIX8='PhagoAssay_Plate8_20201105'
LETTERS8='B,C'
WELL_NUMBERS8='2,3,6,7'
PICTURE_NUMBERS8='1,2,3,4,5'

#OUTPUT DIRECTORY PLATE 8
OUTDIR8=$BASE/Plate8_Merged/
mkdir $OUTDIR8

#RUN SKRIPT PLATE 8
python ./merge_particle_files.py --plate_dir $PLATE_DIR8 --prefix $PREFIX8 --letters $LETTERS8 --well_numbers $WELL_NUMBERS8 --picture_numbers $PICTURE_NUMBERS8 --outdir $OUTDIR8
wait
echo Plate 8 particles merged