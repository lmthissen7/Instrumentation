# For lab 1 of instrumentation--doing the calculations and now the graphs w/ consideration for stablization time
# Lynne Thissen and Nate Peyer
# I have neither given or received, nor have I tolerated others' use of unauthorized aid

# imports
import pandas as pd
import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as pp

# Read data
col_names = ('time', 'temperature')
df_iw_rw = pd.read_csv('fine_iw_rw.TXT', encoding='latin', sep=r'\s+', usecols=[0, 2], names=col_names, header=0)
df_rw_iw = pd.read_csv('fine_rw_iw.TXT', encoding='latin', sep=r'\s+', usecols=[0, 2], names=col_names, header=0)
df_ia_ra = pd.read_csv('standard_ia_ra.TXT', encoding='latin', sep=r'\s+', usecols=[0, 2], names=col_names, header=0)
df_ra_ia = pd.read_csv('standard_ra_ia.TXT', encoding='latin', sep=r'\s+', usecols=[0, 2], names=col_names, header=0)


# Convert time and temperature
def clean_data(df):
    time = pd.to_timedelta(df['time'].str.replace('+', '', regex=False), errors='coerce').dt.total_seconds()
    temperature = pd.to_numeric(df['temperature'], errors='coerce')
    valid = time.notna() & temperature.notna()
    return time[valid].values, temperature[valid].values

# Clean that data!
time_iw_rw, temp_iw_rw = clean_data(df_iw_rw)
time_rw_iw, temp_rw_iw = clean_data(df_rw_iw)
time_ia_ra, temp_ia_ra = clean_data(df_ia_ra)
time_ra_ia, temp_ra_ia = clean_data(df_ra_ia)

# Make those plots girl
# iw to rw
fig, ax = pp.subplots()
pp.plot(time_iw_rw, temp_iw_rw)
ax.set_title('Temperature (°C) vs Time (Seconds)\nIce Water to Room Water (Fine)\nLynne Thissen and Nate Peyer', fontsize = 10)
pp.ylabel('Temperature (°C)')
pp.xlabel('Time (Seconds)')
pp.savefig('iw_rw.png', dpi=300)
# rw to iw
fig, ax = pp.subplots()
pp.plot(time_rw_iw, temp_rw_iw)
ax.set_title('Temperature (°C) vs Time (Seconds)\nRoom Water to Ice Water (Fine)\nLynne Thissen and Nate Peyer', fontsize = 10)
pp.ylabel('Temperature (°C)')
pp.xlabel('Time (Seconds)')
pp.savefig('rw_iw.png')
# ia to ra
fig, ax = pp.subplots()
pp.plot(time_ia_ra, temp_ia_ra)
ax.set_title('Temperature (°C) vs Time (seconds)\nIce Air to Room Air (Standard)\nLynne Thissen and Nate Peyer', fontsize = 10)
pp.ylabel('Temperature (°C)')
pp.xlabel('Time (seconds)')
pp.savefig('ia_ra.png')
# ra to ia
fig, ax = pp.subplots()
pp.plot(time_ra_ia, temp_ra_ia)
ax.set_title('Temperature (°C) vs Time (seconds)\nRoom Air to Ice Air (Standard)\nLynne Thissen and Nate Peyer', fontsize = 10)
pp.ylabel('Temperature (°C)')
pp.xlabel('Time (seconds)')
pp.savefig('ra_ia.png')

# Make reduced datasets for tau 
def reduce_data(time, temperature, cutoff):
    valid = time <= cutoff
    return time[valid], temperature[valid]

calc_time_iw_rw, calc_temp_iw_rw = reduce_data(time_iw_rw, temp_iw_rw, 8)
calc_time_rw_iw, calc_temp_rw_iw = reduce_data(time_rw_iw, temp_rw_iw, 8)
calc_time_ia_ra, calc_temp_ia_ra = reduce_data(time_ia_ra, temp_ia_ra, 75)
calc_time_ra_ia, calc_temp_ra_ia = reduce_data(time_ra_ia, temp_ra_ia, 75)

# calculate!!
# 1/e
def calculate_tau_1e(time, temperature):
    T0 = temperature[0]
    Ta = temperature[-1]
    T_tau = T0 + 0.632 * (Ta - T0)
    index = np.argmin(np.abs(temperature - T_tau))
    return time[index]

# ln
def calculate_tau_ln(time, temperature):
    T0 = temperature[0]
    Ta = temperature[-1]
    y = -np.log((temperature - Ta) / (T0 - Ta))
    valid = np.isfinite(y) & (y > 0)
    slope, intercept, r, p, stderr = linregress(time[valid], y[valid])
    return 1 / slope

# Calculate those time constants
results = {'Ice Water -> Room Water (Fine)': (calculate_tau_1e(calc_time_iw_rw, calc_temp_iw_rw), 
                                              calculate_tau_ln(calc_time_iw_rw, calc_temp_iw_rw)),
           'Room Water -> Ice Water (Fine)': (calculate_tau_1e(calc_time_rw_iw, calc_temp_rw_iw), 
                                              calculate_tau_ln(calc_time_rw_iw, calc_temp_rw_iw)),
           'Ice Air -> Room Air (Standard)': (calculate_tau_1e(calc_time_ia_ra, calc_temp_ia_ra),
                                              calculate_tau_ln(calc_time_ia_ra, calc_temp_ia_ra)),
           'Room Air -> Ice Air (Standard)': (calculate_tau_1e(calc_time_ra_ia, calc_temp_ra_ia),
                                              calculate_tau_ln(calc_time_ra_ia, calc_temp_ra_ia))
}
#Print output please
print('Time Constants:')
for name, (tau_1e, tau_ln) in results.items():
    print(name)
    print(f'  1/e tau = {tau_1e:.2f} seconds')
    print(f'  ln tau  = {tau_ln:.2f} seconds')