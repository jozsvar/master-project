#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


#input file#
mean_file = '/Users/Judit/Desktop/KI_Carl_Sellgren/Master_Thesis/Analysis/TRIAL_FINAL_ANALYSIS_2/phago_assay_mean.tsv'
df = pd.read_csv(mean_file, sep='\t', encoding='utf8')

###FUNCTIONS###
def phenotypes(df, ID, target, title):
	'''selects the data the wanted data and makes a line plot with mean +- SEM
	'''
	data=[]
	
	for i in ID:
		cond=df.loc[df['Condition'] == i]
		data.append(cond)


	data_concat=pd.concat(data)

	#the labels are selected from the dataframe and converted to a list with unique values
	labels=data_concat['Time_point'].unique().tolist()

	#The data for eaach 'D57 Condition' is selected from the dataframe 
	y1=data_concat.loc[data_concat['Condition']==ID[0]]
	y1_to_plot=y1['Mean']
	x1=y1['Time_point']
	SEM1=y1['SEM']

	y2=data_concat.loc[data_concat['Condition']==ID[1]]
	y2_to_plot=y2['Mean']
	x2=y2['Time_point']
	SEM2=y2['SEM']

	y3=data_concat.loc[data_concat['Condition']==ID[2]]
	y3_to_plot=y3['Mean']
	x3=y3['Time_point']
	SEM3=y3['SEM']

	y4=data_concat.loc[data_concat['Condition']==ID[3]]
	y4_to_plot=y4['Mean']
	x4=y4['Time_point']
	SEM4=y4['SEM']

	#the plots are made with errorbars = SEM
	plt.errorbar(x1, y1_to_plot, yerr=SEM1, color='lightsteelblue')
	plt.errorbar(x2, y2_to_plot, yerr=SEM2,color='steelblue')
	plt.errorbar(x3, y3_to_plot, yerr=SEM3,color='lightcoral')
	plt.errorbar(x4, y4_to_plot, yerr=SEM4,color='brown')

	#Labels and X-Axis ticks are determined
	plt.title(title,size = 'xx-large')
	plt.xlabel('Time point (hours)', size='large')
	plt.ylabel('Phase object area of Particles (%)\n/Phase object confluency area of -T1 (%)')
	plt.xticks(np.arange(len(labels)), labels, rotation=45, ha='right', rotation_mode="anchor", size='small')

	#The legend is made 
	HC1=mpatches.Patch(color='lightsteelblue', label = ID[0])
	HC2=mpatches.Patch(color='steelblue', label = ID[1])
	SCZ1=mpatches.Patch(color='lightcoral', label = ID[2])
	SCZ2=mpatches.Patch(color='brown', label = ID[3])

	#The legend is added to the plot
	plt.legend(handles=[HC1, HC2, SCZ1, SCZ2], loc='upper left')
	plt.tight_layout()

	#save plot
	plt.savefig('/Users/Judit/Desktop/KI_Carl_Sellgren/Master_Thesis/Analysis/TRIAL_FINAL_ANALYSIS_2/Curves/phago_curve_'+target+'.png',format='png',dpi=300)
	plt.close()

#function input#
target=['phe','mix']
title=['Phenotype-derived models','Mixed models']
ID_phe=['HC_D57_HC_SYN','HC_D105_HC_SYN','SCZ_D57_SCZ_SYN','SCZ_D105_SCZ_SYN']
ID_mix=['HC_D57_SCZ_SYN','HC_D105_SCZ_SYN','SCZ_D57_HC_SYN','SCZ_D105_HC_SYN']

###MAIN###
phenotypes(df, ID_phe, target[0], title[0])
phenotypes(df, ID_mix, target[1], title[1])
