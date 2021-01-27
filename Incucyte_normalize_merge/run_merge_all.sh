#!/bin/bash -l

###RUNSCRIPT###

BASE=/Volumes/Documents/Lab_work/KI_Carl_Sellgren/Incucyte_Analys/

#Add SCZ_D57_HCsyn 
ADD_FILE=$BASE/D57_D105_norm_avr_files/D57_SCZline_HCsyn_3.tsv
FINAL_FILE=$BASE/D57_D105_norm_avr_files/phago_assay_final_file.tsv
ID='SCZ_D57_HC_SYN'

OUTFILE=$BASE/D57_D105_norm_avr_files/phago_assay_final_file.tsv

python ./merge_all_files.py  --file_to_add $ADD_FILE --final_file $FINAL_FILE --ID $ID --outfile_final $OUTFILE
wait
echo SCZ_D57_HC_SYN added

#Add HC_D57_SCZsyn 
ADD_FILE_1=$BASE/D57_D105_norm_avr_files/D57_HCline_SCZsyn_1.tsv
ID_1='HC_D57_SCZ_SYN'

python ./merge_all_files.py  --file_to_add $ADD_FILE_1 --final_file $FINAL_FILE --ID $ID_1 --outfile_final $OUTFILE
wait
echo HC_D57_SCZ_SYN added


#Add HC_D57_SCZsyn 
ADD_FILE_2=$BASE/D57_D105_norm_avr_files/D57_HCline_HCsyn_1.tsv
ID_2='HC_D57_HC_SYN'

python ./merge_all_files.py  --file_to_add $ADD_FILE_2 --final_file $FINAL_FILE --ID $ID_2 --outfile_final $OUTFILE
wait
echo HC_D57_HC_SYN added


#Add SCZ_D105_SCZ_SYN
ADD_FILE_3=$BASE/D57_D105_norm_avr_files/D105_SCZline_SCZsyn_1.tsv
ID_3='SCZ_D105_SCZ_SYN'

python ./merge_all_files.py  --file_to_add $ADD_FILE_3 --final_file $FINAL_FILE --ID $ID_3 --outfile_final $OUTFILE
wait
echo SCZ_D105_SCZ_SYN added


#Add SCZ_D105_HC_SYN
ADD_FILE_4=$BASE/D57_D105_norm_avr_files/D105_SCZline_HCsyn_2.tsv
ID_4='SCZ_D105_HC_SYN'

python ./merge_all_files.py  --file_to_add $ADD_FILE_4 --final_file $FINAL_FILE --ID $ID_4 --outfile_final $OUTFILE
wait
echo SCZ_D105_HC_SYN added


#Add HC_D105_SCZ_SYN
ADD_FILE_5=$BASE/D57_D105_norm_avr_files/D105_HCline_SCZsyn_3.tsv
ID_5='HC_D105_SCZ_SYN'

python ./merge_all_files.py  --file_to_add $ADD_FILE_5 --final_file $FINAL_FILE --ID $ID_5 --outfile_final $OUTFILE
wait
echo HC_D105_SCZ_SYN added


#Add HC_D105_SCZ_SYN
ADD_FILE_6=$BASE/D57_D105_norm_avr_files/D105_HCline_HCsyn_3.tsv
ID_6='HC_D105_HC_SYN'

python ./merge_all_files.py  --file_to_add $ADD_FILE_6 --final_file $FINAL_FILE --ID $ID_6 --outfile_final $OUTFILE
wait
echo HC_D105_HC_SYN added
wait
echo DONE


