#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.graphics.gofplots import qqplot
from scipy.stats import shapiro
from scipy.stats import normaltest
from scipy.stats import anderson
from scipy.stats import friedmanchisquare 
import scikit_posthocs as sp
import matplotlib.pyplot as plt


'''This code calculates if the significnat differences in the data using Friemdan's test and Con-Post-Hoc Test
'''

###INPUT FILE###
final_file = '/Users/Judit/Desktop/KI_Carl_Sellgren/Master_Thesis/Analysis/TRIAL_FINAL_ANALYSIS_2/phago_assay_final_file.tsv'


###FUNCTIONS###
def remove_pre(final_file):
	'''A function that calculates the 
	'''
	df = pd.read_csv(final_file, sep='\t', encoding='utf8')

	non_pre_rows = []
	pre = df.loc[df['time_point_x'] != 'pre']
	non_pre_rows.append(pre)

	df1 = pd.concat(non_pre_rows)

	return df1

def calculations(df1, outdir):
	'''A function that calculates the MEAN, STANDARD DEVIATION and STANDARD MEAN ERROR of each condition per time point 
	'''
	ID = ['SCZ_D57_SCZ_SYN', 'SCZ_D57_HC_SYN', 'HC_D57_SCZ_SYN', 'HC_D57_HC_SYN', 'SCZ_D105_SCZ_SYN', 'SCZ_D105_HC_SYN', 'HC_D105_SCZ_SYN', 'HC_D105_HC_SYN']
	calc=[]

	for i in ID:
		data=df1.loc[df1['ID'] == i]

		#calculate mean, standard deviation and standard error of mean
		mean = data.groupby('time_point_x')['Normalized_area'].mean().reset_index()
		SD = data.groupby('time_point_x')['Normalized_area'].std().reset_index()
		SEM = data.groupby('time_point_x')['Normalized_area'].sem().reset_index()

		#merge columns on 'time_point_x'
		matched_df = pd.merge(mean, SD,  how='left', on=[u'time_point_x'])
		df = pd.merge(matched_df, SEM, how='left', on=[u'time_point_x'])
		#rename columns
		df.rename(columns={'time_point_x':'Time_point','Normalized_area_x':'Mean', 'Normalized_area_y':'SD', 'Normalized_area':'SEM'}, inplace=True)
		#insert a 'Condition' column with the given condition
		df.insert(0, 'Condition', i)

		calc.append(df)

	df2 = pd.concat(calc)
	df2.to_csv(outdir+'phago_assay_mean.tsv', index=False, sep='\t')

	#calculate if there is a significant difference in the distributions
	friedman(df2,ID)
	#calculate p-values using a multi comparison test 
	post_hoc(df2,ID,outdir)


def norm_dist(df1,outdir):
	'''Test the data if it is normally distributed
	'''
	#Quantile-Quantile Plot 
	qqplot(df1['Normalized_area'], line='s')
	plt.title("Q-Q plot: Phagocytosis Assay")
	plt.savefig(outdir+'phago_assay_qqplot.png', format='png', dpi=300)
	plt.close()

	#Histogram
	plt.hist(df1['Normalized_area'])
	plt.title("Histogram: Phagocytosis Assay")
	plt.savefig(outdir+'phago_assay_histo.png', format='png', dpi=300)
	plt.close()
	
	#Shapiro-Wilk Test: not accuarte for N>5000!
	stat1, p1 = shapiro(df1['Normalized_area'])
	print('Shapiro-Wilk Test: Statistics=%.3f, p=%.3e' % (stat1, p1))

	alpha1 = 0.05
	if p1 > alpha1:
		print('Shapiro-Wilk Test: Sample looks Gaussian (fail to reject H0)')
	else:
		print('Shapiro-Wilk Test: Sample does not look Gaussian (reject H0)')

	#D'Agostino's K^2 Test
	stat2, p2 = normaltest(df1['Normalized_area'])
	print('D Agostinos K^2 Test: Statistics=%.3f, p=%.3e' % (stat2, p2))

	alpha2 = 0.05
	if p2 > alpha2:
		print('D Agostinos K^2 Test: Sample looks Gaussian (fail to reject H0)')
	else:
		print('D Agostinos K^2 Test: Sample does not look Gaussian (reject H0)')

	#Anderson-Darling Test
	result = anderson(df1['Normalized_area'])
	print('Anderson-Darling Test: Statistics= %.3f' % result.statistic)

	p = 0
	for i in range(len(result.critical_values)):
		sl, cv = result.significance_level[i], result.critical_values[i]
		if result.statistic < result.critical_values[i]:
			print('%.3f: %.3f, data looks normal (fail to reject H0)' % (sl, cv))
		else:
			print('%.3f: %.3f, data does not look normal (reject H0)' % (sl, cv))


def friedman(df2, ID):
	'''A function that calculates friedmanchisquare
	'''
	# compare samples on conditions 
	stat, p = friedmanchisquare(df2.loc[df2['Condition'] == ID[0], 'Mean'], df2.loc[df2['Condition'] == ID[1], 'Mean'], 
								df2.loc[df2['Condition'] == ID[2], 'Mean'], df2.loc[df2['Condition'] == ID[3], 'Mean'], 
								df2.loc[df2['Condition'] == ID[4], 'Mean'], df2.loc[df2['Condition'] == ID[5], 'Mean'], 
								df2.loc[df2['Condition'] == ID[6], 'Mean'], df2.loc[df2['Condition'] == ID[7], 'Mean'])

	print('Statistics=%.3f, p=%.3e' % (stat, p))

	#interpret
	alpha = 0.05
	if p > alpha:
		print('Phagocytosis Assay: the different conditions have same distributions (fail to reject H0)')
	else:
		print('Phagocytosis Assay: the different conditions have different distributions (reject H0)')


def post_hoc(df2,ID,outdir):
	'''Multiple comparison Conver test 
	'''
	mc = sp.posthoc_conover_friedman(df2, y_col='Mean', block_col='Time_point', group_col='Condition', melted=True, p_adjust='holm')
	value = np.array(np.log10(mc))
	mc.to_csv(outdir+'phago_assay_pvals.tsv', index=False, sep='\t')
	table = sp.sign_table(mc)
	table.to_csv(outdir+'phago_assay_sign_table.tsv', index=False, sep='\t')
	
	#create heatmap with p-values
	heat_map(value,ID,outdir)


def heat_map(value,ID,outdir):
	'''plots a heatmap with the p-values in the squares (3 decimals) 
	'''
	#rounds the values to 3 decimals
	values_r=np.around(value, decimals=2)

	fig, ax = plt.subplots()
	plt.imshow(value)

	#adds the p-values to each square
	for i in range(len(ID)):
		for j in range(len(ID)):
			text = plt.text(j, i, values_r[i, j],ha="center", va="center",stretch='condensed', color="w", size='x-small', weight='semibold')
	
	plt.xticks(np.arange(len(ID)),labels=ID,rotation=45, ha="right",
         rotation_mode="anchor", size='medium')
	plt.yticks(np.arange(len(ID)),labels=ID, size='medium')
	plt.colorbar().set_label('log10 p-value', size='medium')
	plt.title('p-values', size='xx-large')
	plt.tight_layout()
	plt.savefig(outdir+'phago_assay_pvals.png', format='png', dpi=300)
	plt.close()

	return None

##fuction inputs##
outdir='/Users/Judit/Desktop/KI_Carl_Sellgren/Master_Thesis/Analysis/TRIAL_FINAL_ANALYSIS_2/'

###MAIN###
df1=remove_pre(final_file)
calculations(df1,outdir)
norm_dist(df1,outdir)



