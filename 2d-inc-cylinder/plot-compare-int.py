import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig, ax = plt.subplots(1, 1, figsize=(5, 3))


df1  = pd.read_csv('int_esdirk23.csv')
df2  = pd.read_csv('int_sdirk33.csv')
#df3  = pd.read_csv('int_sdirk43.csv')
df4  = pd.read_csv('int_esdirk35.csv')


# Plot only the fifth entry

ax.plot(df1['t'], df1['int-E'], '--', label=r'$ESDIRK23$', linewidth=3)
ax.plot(df2['t'], df2['int-E'], label=r'$SDIRK33$', linewidth=2)
#ax.plot(df3['t'], df3['int-E'], '--', label=r'$SDIRK43$', linewidth=3)
ax.plot(df4['t'], df4['int-E'], label=r'$ESDIRK35$', linewidth=2)

ax.set_xlabel(r'$n$')
ax.legend(loc='best')

plt.tight_layout()
plt.savefig('int.png', dpi=300)
plt.close()
