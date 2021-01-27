#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.stats as sp
import seaborn as sns
import numpy as np
from scipy import stats
import scikit_posthocs as sp

'''Here, on the one hand the fold change (data is plotted) between groups is calculated as well as Kruskal–Wallis Test and subsequent Dunn's Test 
(multiple comparison) and these p-values are plotted in a heatmap. Finally the data is plotted in a violin plot
'''

###Input files###
pcr_data = '/Users/Judit/Desktop/KI_Carl_Sellgren/Master_Thesis/Analysis/Analysis_q_RT_PCR/qRTPCR_astros.tsv'

#read file
df = pd.read_csv(pcr_data, sep='\t', encoding='utf8')


####FUNCTION####

def fc(df, ID, target, outdir):
	'''Calculates the log2 fold change of (log2(mean(post)/mean(pre))) and outputs a plot
	'''
	#creates a dataframe with the means/group
	mean = df.groupby(['ID'])['values'].mean()

	mean_list = mean.values.tolist()
	#List order: HC-D105, HC-D57, SCZ-D105, SCZ-D57

	log2FC = []
	
	#log2 fold change: HC_105/SCZ_57
	log2FC_2 = np.log2(mean_list[0]/mean_list[3])
	#append to list
	log2FC.append(log2FC_2)
	#log2 fold change: SCZ_105/HC_57
	log2FC_1 = np.log2(mean_list[2]/mean_list[1])
	#append to list
	log2FC.append(log2FC_1)	
	#log2 fold change: SCZ_105/HC_105
	log2FC_105 = np.log2(mean_list[2]/mean_list[0])
	#append to list
	log2FC.append(log2FC_105)	
	#log2 fold change: SCZ_57/HC_57
	log2FC_57 = np.log2(mean_list[3]/mean_list[1])
	#append to list
	log2FC.append(log2FC_57)	
	#log2 fold change: SCZ_105/SCZ_57
	log2FC_SCZ = np.log2(mean_list[2]/mean_list[3])
	#append to list
	log2FC.append(log2FC_SCZ)
	#log2 fold change: HC_105/HC_57
	log2FC_HC = np.log2(mean_list[0]/mean_list[1])
	#append to list
	log2FC.append(log2FC_HC)
	
	#create dataframe
	results = pd.DataFrame()
	results['ID'] = ID 
	results['log2FC_'+target] = log2FC

	#Plot the fold chnage data 
	results['log2FC_'+target].plot(kind='barh',
                    color=(results['log2FC_'+target] > 0).map({True: 'indigo',
                                                    False: 'yellowgreen'}))
	
	plt.yticks(np.arange(len(ID)),labels=ID, size='large')
	plt.xticks(size='large')
	plt.xlabel('Fold change (log2)', size='large')
	#draws a vertical line at 0
	plt.vlines(0,-1,6,color='k', linewidth=0.7)
	plt.title('Fold change ('+target+')', size='xx-large')
	plt.tight_layout()
	plt.savefig(outdir+'Figures/fold_change_'+target+'.png', format='png', dpi=300)
	plt.close()

	return results
	
def stat(df, target, outdir):
	'''Statistical tests: 
	1) Kruskal–Wallis one-way analysis of variance: tests whether samples originate from the same distribution
	2) Dunn's test using a Bonferonni correction
	'''
	
	#GFAP groups 
	groups_gfap = ['HC_57_GFAP','HC_105_GFAP','SCZ_57_GFAP','SCZ_105_GFAP']
	#make a list out of the values to input in Dunn's test 
	g1=list(np.array(df.loc[df['ID'] == groups_gfap[0],'values']))
	g2=list(np.array(df.loc[df['ID'] == groups_gfap[1],'values']))
	g3=list(np.array(df.loc[df['ID'] == groups_gfap[2],'values']))
	g4=list(np.array(df.loc[df['ID'] == groups_gfap[3],'values']))
	gfap=[g1, g2, g3, g4]
	
	#AQP4 groups
	groups_aqp4 = ['HC_57_AQP4','HC_105_AQP4','SCZ_57_AQP4','SCZ_105_AQP4']
	#make a list out of the values to input in Dunn's test 
	a1=list(np.array(df.loc[df['ID'] == groups_aqp4[0],'values']))
	a2=list(np.array(df.loc[df['ID'] == groups_aqp4[1],'values']))
	a3=list(np.array(df.loc[df['ID'] == groups_aqp4[2],'values']))
	a4=list(np.array(df.loc[df['ID'] == groups_aqp4[3],'values']))
	aqp4 = [a1, a2, a3, a4]
	
	#Kruskal-Wallis test for GFAP expression
	stat1, p1 = stats.kruskal(np.array(df.loc[df['ID'] == groups_gfap[0],'values']),np.array(df.loc[df['ID'] == groups_gfap[1],'values']),
								np.array(df.loc[df['ID'] == groups_gfap[2],'values']),np.array(df.loc[df['ID'] == groups_gfap[3],'values']),nan_policy='omit')

	print('Kruskal–Wallis test for '+target[0]+' expression: Statistics=%.3f, p=%.3e' % (stat1, p1))

	#perform Dunn's test using a Holm-Bonferonni correction for the p-values
	mc1 = sp.posthoc_dunn(gfap, p_adjust = 'holm')
	values1 = np.array(np.log10(mc1))
	mc1.to_csv(outdir+'dunns_gfap.tsv', index=False, sep='\t')
	table1 = sp.sign_table(mc1)
	table1.to_csv(outdir+'sign_table_gfap.tsv', index=False, sep='\t')

	#create heatmap with p-values
	heat_map(values1, target[0], outdir)

	#Kruskal-Wallis test for AQP4 expression
	stat2, p2 = stats.kruskal(np.array(df.loc[df['ID'] == groups_aqp4[0],'values']),np.array(df.loc[df['ID'] == groups_aqp4[1],'values']),
								np.array(df.loc[df['ID'] == groups_aqp4[2],'values']),np.array(df.loc[df['ID'] == groups_aqp4[3],'values']),nan_policy='omit')

	print('Kruskal–Wallis test for '+target[1]+' expression: Statistics=%.3f, p=%.3e' % (stat2, p2))

	#perform Dunn's test using a Holm-Bonferonni correction for the p-values
	mc2 = sp.posthoc_dunn(aqp4, p_adjust = 'holm')
	values2 = np.array(np.log10(mc2))
	mc2.to_csv(outdir+'dunns_aqp4.tsv', index=False, sep='\t')
	table2 = sp.sign_table(mc2)
	table2.to_csv(outdir+'sign_table_aqp4.tsv', index=False, sep='\t')
	
	#create heatmap with p-values
	heat_map(values2, target[1], outdir)


def heat_map(values, target, outdir):
	'''plots a heatmap with the p-values in the squares (3 decimals) 
	'''
	ticks=['HC_D57','HC_D105','SCZ_D57','SCZ_D105']
	#rounds the values to 3 decimals
	values_r=np.around(values, decimals=3)

	fig, ax = plt.subplots()
	plt.imshow(values)

	#adds the p-values to each square
	for i in range(len(ticks)):
		for j in range(len(ticks)):
			text = plt.text(j, i, values_r[i, j],ha="center", va="center",stretch='condensed', color="w", size='large', weight='semibold')
	
	plt.xticks(np.arange(len(ticks)),labels=ticks,rotation=45, ha="right",
         rotation_mode="anchor", size='large')
	plt.yticks(np.arange(len(ticks)),labels=ticks, size='large')
	plt.colorbar().set_label('log10 p-value', size='large')
	plt.title('p-values ('+target+')', size='xx-large')
	plt.tight_layout()
	plt.savefig(outdir+'Figures/pvals_'+target+'.png', format='png', dpi=300)
	plt.close()

	return None


def make_plot(df, outdir):
	'''uses seaborn to plot the data in a violin plot 
	'''
	df["values"]=np.log10(df["values"])
	for gene in ['GFAP','AQP4']:
		sel = df[df['target']==gene]
		fig,ax = plt.subplots(figsize=(9/2.54,9/2.54))
		sns.catplot(x="TP", y="values", 
			hue="phenotype", data=sel, kind="violin", legend=False,
			palette=sns.color_palette(['steelblue','lightcoral']))
		plt.ylabel('Relative Expression (log10)', size='large')
		#plt.yticks(np.arange(-8,-3,step=0.5))
		plt.xlabel('Time point (days)', size='large')
		plt.title(gene, size='xx-large')
		plt.legend(loc='lower right', fancybox=True)
		plt.tight_layout()
		plt.savefig(outdir+'Figures/'+gene+'.png',format='png',dpi=300)
		plt.close()


#Function inputs##
target=['GFAP','AQP4']
df_gfap=df.loc[df['target'] == target[0]]
df_aqp4=df.loc[df['target'] == target[1]]
ID = ['SCZ-D57 vs. HC-D105','HC-D57 vs. SCZ-D105','D105','D57','SCZ','HC'] 
outdir='/Users/Judit/Desktop/KI_Carl_Sellgren/Master_Thesis/Analysis/Analysis_q_RT_PCR/'

####MAIN#####
gfap=fc(df_gfap, ID, target[0], outdir)
aqp4=fc(df_aqp4, ID, target[1], outdir)
stat(df, target, outdir)
make_plot(df, outdir)

#merge fold change files and save as tsv
df1=pd.merge(gfap, aqp4,  how='left', on=['ID'])
df1.to_csv('/Users/Judit/Desktop/KI_Carl_Sellgren/Master_Thesis/Analysis/Analysis_q_RT_PCR/fold_change_astros.tsv',index=False, sep='\t')





