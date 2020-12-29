#!/bin/bash -l

###RUNSCRIPT###

BASE=/Volumes/Documents/Lab_work/KI_Carl_Sellgren/Incucyte_Analys/


###Merge all files with new ID coloumn, the timepoint and the Normalized %Area###
#Initial file creation from D57_SCZ_SCZsyn
SORT_DATA=$BASE/D57_D105_norm_avr_files/D57_SCZline_SCZsyn_3.tsv
ID='SCZ_D57_SCZ_SYN'
OUTFILE=$BASE/D57_D105_norm_avr_files/phago_assay_final_file.tsv

python ./create_final_file.py --sort_data_file $SORT_DATA --ID $ID --outfile_final $OUTFILE
wait
echo Final file created