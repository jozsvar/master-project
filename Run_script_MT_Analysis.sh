#!/bin/bash -l

###RUNSCRIPT###

BASE=/Volumes/Documents/Lab_work/KI_Carl_Sellgren/Incucyte_Analys/

###MERGE PARTICLE FILES###
#bash ./run_particles.sh


###MERGE CONFLUENCY FILES###
#bash ./run_confluency.sh


###NORMALIZE DATA###
#bash ./run_normalization.sh

###AVERAGE WELLS###
#bash ./run_average_same_line.sh

###CREAT FILES FOR EACH CONDITION###
#bash ./run_merge_conditions.sh


###CREATE FINAL FILE###
bash ./run_create_final.sh

###MERGE ALL FILES###
bash ./run_merge_all.sh