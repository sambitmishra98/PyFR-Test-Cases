
# We open the file /home/sambit/github/Improvements/PyFR-Test-Cases/2d-inc-cylinder/pseudodt_esdirk35_pi_pi.csv

# pseudo-steps, tcurr,n,res,res_p,res_u,res_v,min,min_p,min_u,min_v,max,max_p,max_u,max_v
# 68,75.5,68,0.002004957039637707,0.0018407327364540948,5.569253702593814e-05,0.00010853176615767384,0.0029008412664844243,0.0029008412664844243,0.006,0.006,0.006,0.006,0.006,0.006
# 128,75.9950495049505,60,0.0020349344908655374,0.001856749721805136,6.360919818954342e-05,0.00011457557087085801,0.0025475497419268915,0.0025475497419268915,0.005940594059405941,0.005940594059405941,0.005940594059405941,0.005940594059405941,0.005940594059405941,0.005940594059405941
# 188,76.4950495049505,60,0.002115950084648719,0.0019339500234109555,6.645430011477525e-05,0.00011554576112298834,0.002529046658091646,0.002529046658091646,0.006,0.006,0.006,0.006,0.006,0.006
# 248,77.0000495049505,60,0.0020465809405418632,0.0018602098290556868,6.747782175446644e-05,0.00011889328973171028,0.0027904057774030115,0.0027904057774030115,0.00606,0.00606,0.00606,0.00606,0.00606,0.00606
# 308,77.5100995049505,60,0.0020520896390675697,0.0018690493301184762,6.314401649623311e-05,0.00011989629245286045,0.002959738558539867,0.002959738558539867,0.006120599999999999,0.006120599999999999,0.006120599999999999,0.006120599999999999,0.006120599999999999,0.006120599999999999
# 368,78.02525000495051,60,0.0021210313722669068,0.0019368777276029736,6.373079826307633e-05,0.00012042284640085677,0.0025106832506036907,0.0025106832506036907,0.006181805999999999,0.006181805999999999,0.006181805999999999,0.006181805999999999,0.006181805999999999,0.006181805999999999

# We plot in 4 subplots, one for residuals, one for mins, one for maxs and one for n. All plots are with tcurr as x-axis.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

# Read the csv file
df = pd.read_csv('/home/sambit/github/Improvements/PyFR-Test-Cases/2d-inc-cylinder/pseudodt_esdirk35_pi_pi.csv')

# Create a figure instance
fig, ax = plt.subplots(2,2)

# Plot the first subplot
ax[0,0].semilogy(df['tcurr'], df['res_p'], label = 'p')
ax[0,0].semilogy(df['tcurr'], df['res_u'], label = 'u')
ax[0,0].semilogy(df['tcurr'], df['res_v'], label = 'v')
ax[0,0].set_title('Residuals')
ax[0,0].set_xlabel('tcurr')
ax[0,0].set_ylabel('res')
ax[0,0].legend(loc='upper left')

# Plot the second subplot
ax[0,1].plot(df['tcurr'], df['min_p'], label = 'p')
ax[0,1].plot(df['tcurr'], df['min_u'], label = 'u')
ax[0,1].plot(df['tcurr'], df['min_v'], label = 'v')
ax[0,1].set_title('Mins')
ax[0,1].set_xlabel('tcurr')
ax[0,1].set_ylabel('min')
ax[0,1].legend(loc='upper left')
    
# Plot the third subplot
ax[1,0].plot(df['tcurr'], df['max_p'], label = 'p')
ax[1,0].plot(df['tcurr'], df['max_u'], label = 'u')
ax[1,0].plot(df['tcurr'], df['max_v'], label = 'v')
ax[1,0].set_title('Maxs')
ax[1,0].set_xlabel('tcurr')
ax[1,0].set_ylabel('max')
ax[1,0].legend(loc='upper left')

# Plot the fourth subplot
ax[1,1].plot(df['tcurr'], df['n'])
ax[1,1].set_title('n')
ax[1,1].set_xlabel('tcurr')
ax[1,1].set_ylabel('n')

# Adjust the padding between and around subplots
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)

# Save the figure
plt.savefig('pseudodt_esdirk35_pi_pi.png')
    

