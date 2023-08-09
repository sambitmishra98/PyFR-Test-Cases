import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig, (ax, ax2) = plt.subplots(2, 1, figsize=(20, 5))

df11  = pd.read_csv('int_esdirk35_none.csv')
df12  = pd.read_csv('int_esdirk35_pi.csv')
df2   = pd.read_csv('int_sdirk33.csv')

# Get the difference in `t` column and plot
df11['t-diff'] = df11['t'].diff()
df12['t-diff'] = df12['t'].diff()
df2['t-diff']  = df2['t'].diff()

# Plot t-diff
ax.plot(df11['t'], df11['t-diff'], label=r'$ESDIRK35-None$')
ax.plot(df12['t'], df12['t-diff'], label=r'$ESDIRK35-PI$')
ax.plot(df2[ 't'], df2[ 't-diff'], label= r'$SDIRK33$')
ax.set_xlabel(r'$t$')
ax.legend(loc='best')

ax2.plot(df11['t'], df11['int-E'], label=r'$ESDIRK35-None$')
ax2.plot(df12['t'], df12['int-E'], label=r'$ESDIRK35-PI$')
ax2.plot(df2[ 't'], df2[ 'int-E'], label= r'$SDIRK33$')
ax2.set_xlabel(r'$t$')
ax2.legend(loc='best')

plt.tight_layout()
plt.savefig('dt.png')
plt.close()
