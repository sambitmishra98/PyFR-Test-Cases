# Plot the data in /home/sambit/github/Improvements/PyFR-Test-Cases/tgv/dtstats.csv

# n,t,dt,action,error
#0,0.0,0.0005,accept,0.00025504205776635634
#1,0.0005,0.00125,accept,0.003777959692463166
#2,0.00175,0.0010386640330537476,accept,0.002013908014249298
#3,0.002788664033053748,0.0014215188800083636,accept,0.005067305713881499
#4,0.004210182913062112,0.001490403228357261,accept,0.005812851310830408

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('/home/sambit/github/Improvements/PyFR-Test-Cases/tgv/inc_dtstats.csv')

# Take the difference between the time steps, and normalise with the previous step
# Expand the above, without using pd.diff
df['dt-diff'] = (df['dt'].shift(-1) - df['dt'])/df['dt']

# Plot the data in /home/sambit/github/Improvements/PyFR-Test-Cases/tgv/dtstats.csv
fig, ax = plt.subplots()
ax.plot(df['t'], df['dt-diff'], label='dt')
ax.set_xlabel('t')
ax.set_ylabel('(dt-dtpast)/dt')
ax.legend()

plt.show()

plt.savefig('inc_dt.png')
