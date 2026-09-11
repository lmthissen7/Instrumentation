# this code is for lab 1 of instrumentation--time response
#Lynne Thissen and Nathaniel Peyer
#I have neither given or received, nor have I tolerated others' use of unauthorized aid

#import statements
import pandas as pd
import matplotlib.pyplot as pp
import numpy as np 

# read in the data from txt files
# sep ='\s+' is the same as delim_whitespace = true
col_names = ('ms', 'CH01')
df_iw_rw = pd.read_csv('fine_iw_rw.TXT', encoding = 'latin', header = 0, sep = '\\s+', usecols = [0,2], names = col_names)

df_rw_iw = pd.read_csv("fine_rw_iw.TXT", encoding = 'latin', header = 0, sep = '\\s+', usecols = [0,2], names = col_names)

df_ia_ra = pd.read_csv("standard_ia_ra.TXT", encoding = 'latin', header = 0, sep = '\\s+', usecols = [0,2], names = col_names)

df_ra_ia = pd.read_csv("standard_ra_ia.TXT", encoding = 'latin', header = 0, sep = '\\s+', usecols = [0,2], names = col_names)

# iw_rw

#convert ms to s 
time_iw_rw = df_iw_rw['ms'].values
temperature_iw_rw = df_iw_rw['CH01'].values

#plot that data, girl!
fig, ax = pp.subplots()
pp.plot(time_iw_rw, temperature_iw_rw)
ax.set_title('Temperature (°C) vs Time (Seconds)\nIce Water to Room Water Fine\nLynne Thissen and Nate Peyer', fontsize = 10)
pp.ylabel('Temperature (°C)')
pp.xlabel('Time (Seconds)')
pp.savefig('instrumentation_lab1_thissen_peyer.png', dpi=300)


# rw_iw

# Converting the time from ms to s.
time_rw_iw = df_rw_iw['ms'].values
temperature_rw_iw = df_rw_iw['CH01'].values

# Plotting the data to oberseve which data point are irrevlivent.
fig, ax = pp.subplots()
pp.plot(time_rw_iw, temperature_rw_iw)
ax.set_title('Temperature (°C) vs Time (Seconds)\nRoom Water to Ice Water Fine\nLynne Thissen and Nate Peyer', fontsize = 10)
pp.ylabel('Temperature (°C)')
pp.xlabel('Time (Seconds)')
pp.savefig('instrumentation_lab1_thissen_peyer_rw_iw.png', dpi=300)

# ia_ra

# Converting the time from ms to s.
time_ia_ra = df_ia_ra['ms'].values
temperature_ia_ra = df_ia_ra['CH01'].values

# Plotting the data to oberseve which data point are irrevlivent.
fig, ax = pp.subplots()
pp.plot(time_ia_ra, temperature_ia_ra)
ax.set_title('Temperature (°C) vs Time (Seconds)\nIce Air to Room Air Fine\nLynne Thissen and Nate Peyer', fontsize = 10)
pp.ylabel('Temperature (°C)')
pp.xlabel('Time (Seconds)')
pp.savefig('instrumentation_lab1_thissen_peyer_ia_ra.png', dpi=300)

# ra_ia

# Converting the time from ms to s.
time_ra_ia = df_ra_ia['ms'].values
temperature_ra_ia = df_ia_ra['CH01'].values

# Plotting the data to oberseve which data point are irrevlivent.
fig, ax = pp.subplots()
pp.plot(time_ra_ia, temperature_ra_ia)
ax.set_title('Temperature (°C) vs Time (Seconds)\nRoom Air to Ice Air Fine\nLynne Thissen and Nate Peyer', fontsize = 10)
pp.ylabel('Temperature (°C)')
pp.xlabel('Time (Seconds)')
pp.savefig('instrumentation_lab1_thissen_peyer_ra_ia.png', dpi=300)




# Math functions
# The function to calculate the y-axis values
def calculateYaxis(T, T_a, T_o):
    step1 = (T - T_a) / (T_o - T_a)
    tau = np.log(step1)*-1
    return tau 
