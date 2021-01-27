import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.graphics.gofplots import qqplot
from scipy.stats import shapiro
from scipy.stats import normaltest
from scipy.stats import anderson
from matplotlib import pyplot


'''This code tests in different ways, if the data is normally distributed
'''

###Input files###

pcr_data = '/Users/Judit/Desktop/KI_Carl_Sellgren/Master_Thesis/Analysis/Analysis_q_RT_PCR/qRTPCR_astros.tsv'
#read file
df = pd.read_csv(pcr_data, sep='\t', encoding='utf8')


###FUNCTIONS###

def norm_test(df,target):
	'''Tests if the target gene data is normally distributed
	'''
	
	#select all rows that contain the target gene in the 'target' column
	df1 = df.loc[df['target'] == target]
	
	#PLOT DATA
	#Quantile-Quantile Plot 
	qqplot(df1['values'], line='s')
	pyplot.title('Q-Q plot: +'target)
	pyplot.show()

	#Histogram
	pyplot.hist(df1['values'])
	pyplot.title('Histogram: '+target)
	pyplot.show()

	#CALCULATE NORMALITY TESTS
	#Shapiro-Wilk Test
	stat1, p1 = shapiro(df1['values'])
	print('Shapiro-Wilk Test: Statistics=%.3f, p=%.3e' % (stat1, p1))

	alpha1 = 0.05
	if p1 > alpha1:
		print('Shapiro-Wilk Test for '+target+': Sample looks Gaussian (fail to reject H0)')
	else:
		print('Shapiro-Wilk Test for '+target+': Sample does not look Gaussian (reject H0)')

	#D'Agostino's K^2 Test
	stat2, p2 = normaltest(df1['values'])
	print('D Agostinos K^2 Test for '+target+': Statistics=%.3f, p=%.3e' % (stat2, p2))

	alpha2 = 0.05
	if p2 > alpha2:
		print('D Agostinos K^2 Test for '+target+': Sample looks Gaussian (fail to reject H0)')
	else:
		print('D Agostinos K^2 Test for '+target+': Sample does not look Gaussian (reject H0)')

	#Anderson-Darling Test
	result = anderson(df1['values'])
	print('Anderson-Darling Test for '+target+': Statistic: %.3f' % result.statistic)

	p = 0
	for i in range(len(result.critical_values)):
		sl, cv = result.significance_level[i], result.critical_values[i]
		if result.statistic < result.critical_values[i]:
			print('%.3f: %.3f, data looks normal (fail to reject H0)' % (sl, cv))
		else:
			print('%.3f: %.3f, data does not look normal (reject H0)' % (sl, cv))


#Input into function#
target = ['GFAP','AQP4']

###MAIN###
norm_test(df, target[0])
norm_test(df, target[1])