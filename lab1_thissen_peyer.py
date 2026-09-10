# this code is for lab 1 of instrumentation--time response
#lynne thissen and nate peyer
#I have neither given or received, nor have I tolerated others' use of unauthorized aid

#import statements
import pandas as pd
import matplotlib.pyplot as pp
import numpy as np 

#read in txt
col_names = ('ms', 'CH01')
df_iw_rw = pd.read_csv('fine_iw_rw.TXT', encoding='latin', header=0, delim_whitespace=True, usecols=[0,2], names=col_names)

"""
rw_iw_df = pd.read_csv("fine_rw_iw.TXT", encoding='latin', header=2, delim_whitespace=True,
                      usecols[0,2],
                      names=col_names)
ia_ra_df = pd.read_csv("standard_ia_ra.TXT", encoding='latin', header=2, delim_whitespace=True,
                      usecols[0,2],
                      names=col_names)
ra_ia_df = pd.read_csv("standard_ia_ra.TXT", encoding='latin', header=2, delim_whitespace=True,
                      usecols[0,2],
                      names=col_names)
"""
#convert ms to s 
time = df_iw_rw['ms'].values
temperature = df_iw_rw['CH01'].values

#plot that data, girl!
fig, ax = pp.subplots()
pp.plot(time, temperature)
ax.set_title('Temperature (°C) vs Time (Seconds)\nIce Water to Room Water Fine\nLynne Thissen and Nate Peyer', fontsize = 10)
pp.ylabel('Temperature (°C)')
pp.xlabel('Time (Seconds)')
pp.savefig('instrumentation_lab1_thissen_peyer.png', dpi=300)



