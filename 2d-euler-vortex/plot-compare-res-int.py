import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig, ax = plt.subplots(1, 1, figsize=(5, 3))


df1  = pd.read_csv('esdirk23-int.csv')
df2  = pd.read_csv('sdirk33-int.csv')
df3  = pd.read_csv('sdirk43-int.csv')
df4  = pd.read_csv('esdirk35-int.csv')


# Plot only the fifth entry

ax.plot(df1['t'], df1['int-E'], '--', label=r'$ESDIRK23$', linewidth=3)
ax.plot(df2['t'], df2['int-E'], label=r'$SDIRK33$', linewidth=2)
ax.plot(df3['t'], df3['int-E'], '--', label=r'$SDIRK43$', linewidth=3)
ax.plot(df4['t'], df3['int-E'], label=r'$ESDIRK35$', linewidth=2)

ax.set_xlabel(r'$n$')
ax.legend(loc='best')

plt.tight_layout()
plt.savefig('int.png', dpi=300)
plt.close()
