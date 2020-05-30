#!/usr/bin/env python3
# shebang for linux

"""
descriptive_statistics.py
Caculates and plots a number of descriptive statistics on an example dataset.

Descriptive statistics describe the basic features of a dataset in order to establish its validity.
1) PLOT DISTRIBUTION - to establish distribution for future analysis and check for bias (systematic errors such as sampling not being representative of population in some way)
    - Histogram
2) IDENTIFY OUTLIERS - to remove results due to experemental error
    - Scatter plot
3) DESCRIPTIVE STATISTICS - describe characteristics of the dataset
    - Quantity of data (sample size, should be selected from power analysis)
        rules of thumb for continous data can be given:
            Average value in population (10)
            Amount of variation in population (30)
            Freuency of values in catagories (20)
            Relationships between variables (30)
            Stability over time (30)
    - Mean (sum / count, skued by outliers so for normaly distributed data only)
    - Median (middle value, less skued by outliers)
    - Mode (most frequent values, sutable for discrete data or heavily skued bimodal data)
    - Confidence Interval Estimate (range within which the population truth is estimated to lie with a given probability)
    - Range (the difference between smallest and largest values)
    - Inter quatile range (range of the middle 50% datapoints)
    - Standard deviation (average distance that each data point is from the mean. Only valid for normal data)
    - Z-score (# of standard deviations each point is from the mean)
    - Standard error (estimated variation of the sample mean around the population mean)
"""

import pandas as pd
import numpy as np
import scipy as sp
from scipy import stats
from scipy.optimize import curve_fit
from sklearn.preprocessing import MinMaxScaler, normalize
import matplotlib.pyplot as plt

#create example normally distributed data
mu = 0; #mean value (center of bell curve)
sigma = 1; #standard deviation (spread or “width”) of the distribution
size = 1000;
y = np.random.normal(mu, sigma, size);
x = np.linspace(0, size, num=size);

#plot histogram
plt.figure();
bins = 20; #choose between 5 and 20 bins depending on dataset size
plt.hist(y, bins);
plt.title("Histogram");
plt.xlabel("Data Reading Number (Counts)");
plt.ylabel("Frequency (Counts)");
plt.grid(True);

#0-1 normalise data
norm_y = [(i - np.min(y)) / (np.max(y) - np.min(y)) for i in y];

#plot scatter graph
plt.figure();
plt.scatter(x, norm_y);
plt.title("Values over Time to Identify Outliers");
plt.xlabel("Data Reading (Time)");
plt.ylabel("0-1 Normalised Value");
plt.grid(True);

#compute averages
len = len(y);
mean = np.mean(y);
median = np.median(y);
mode = stats.mode(y)[0][0];
mode_count = stats.mode(y)[1][0];
range = np.max(y) - np.min(y);
iqrange = stats.iqr(y);
std_dev = np.std(y);
z_score = stats.zscore(y);
std_err = stats.sem(y);
con_inter = stats.bayes_mvs(y, alpha=0.95); #95% confidence interval for mean, var, and std reported as (center, (lower, upper))

#plot z scores scatter graph
plt.figure();
plt.scatter(x, z_score);
plt.title("Z-Scores of Data Points");
plt.xlabel("Data Reading (Time)");
plt.ylabel("Z-Score");
plt.grid(True);

#print descriptive statistics
print("-------------------------------------");
print("|       DESCRIPTIVE  STATISTICS      |");
print("|  qty of data: {:+d}                |".format(len));
print("|         mean: {:+4.3f}               |".format(mean));
print("| mean c.inter: {:+4.3f}               |".format(con_inter[0][1][1] - con_inter[0][1][0]));
print("|       median: {:+4.3f}               |".format(median));
print("|         mode: {:+4.3f} (count: {:d})    |".format(mode, mode_count));
print("|        range: {:+4.3f}               |".format(range));
print("|     iq range: {:+4.3f}               |".format(iqrange));
print("|      std dev: {:+4.3f}               |".format(std_dev));
print("|      std err: {:+4.3f}               |".format(std_dev));
print("-------------------------------------");

plt.show();
