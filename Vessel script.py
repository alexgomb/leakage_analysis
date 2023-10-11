# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 15:02:03 2023

@author: Alex
"""
#imprt the libraries for data frame
import pandas as pd
import matplotlib.pyplot as plt
#import the file as a data frame and use dropna()
data = pd.read_excel('Leakage data.xlsx').dropna()

#first we select the data we need
data['Rspot average'] = data.iloc[0:, 6:10].mean(axis = 1)
#calculate the net lesion fluorecescence
data['Net lesion fluorescence'] = data.iloc[0:, 5] - data.iloc[0:, 10]
#calculate the normalized lesion index
data['NLI'] = data.iloc[0:, 4] * data.iloc[0:, 11]
#now we have to extract the data from main dataframe and calculate the mean
day_3_mean = data[data['Day'] == 3][['NLI']].mean()
day_5_mean = data[data['Day'] == 5][['NLI']].mean()
day_7_mean = data[data['Day'] == 7][['NLI']].mean()
day_21_mean = data[data['Day'] == 21][['NLI']].mean()
#now we have to calculate the sd
day_3_sd = data[data['Day'] == 3][['NLI']].std()
day_5_sd = data[data['Day'] == 5][['NLI']].std()
day_7_sd = data[data['Day'] == 7][['NLI']].std()
day_21_sd = data[data['Day'] == 21][['NLI']].std()
#merge all the series together deleting the index
day_means = pd.concat([day_3_mean, day_5_mean, day_7_mean, day_21_mean]).reset_index(drop=True)
day_sd = pd.concat([day_3_sd, day_5_sd, day_7_sd, day_21_sd]).reset_index(drop=True)
#juntamos todo en un dataframe
plot_data = pd.DataFrame([day_means, day_sd])
plot_data.columns = ['Day 3', 'Day 5', 'Day 7', 'Day 21']
plot_data.index = ['Mean', 'SD']
#now finally lets plot
plot_data.T.plot(kind='bar', y=['Mean'], color=['red'], yerr='SD', capsize=5, legend=False, ylabel = 'NLI')
