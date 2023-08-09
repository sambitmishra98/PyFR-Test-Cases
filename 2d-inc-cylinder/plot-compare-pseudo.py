import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig, (ax, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 5))


df1  = pd.read_csv('res_esdirk23.csv')
df2  = pd.read_csv('res_sdirk33.csv')
df4  = pd.read_csv('res_esdirk35.csv')

# Plot only the fifth entry

ax.semilogy(df2['t'][::15]  , df2['p'][::15],  label=r'$SDIRK33$')
ax.semilogy(df1['t'][10::11], df1['p'][10::11],  label=r'$ESDIRK23$')
ax.semilogy(df4['t'][20::21], df4['p'][20::21],  label=r'$ESDIRK35$')

ax.set_xlabel(r'$t$')

ax2.semilogy(df1['n'][:11], df1['p'][:11],  label=r'$ESDIRK23$')
ax2.semilogy(df2['n'][:15], df2['p'][:15],  label=r'$SDIRK33$')
ax2.semilogy(df4['n'][:21], df4['p'][:21],  label=r'$ESDIRK35$')
ax2.scatter(df1['n'][10], df1['p'][10], s=100, facecolors='none', edgecolors='C0')
ax2.scatter(df2['n'][14], df2['p'][14], s=100, facecolors='none', edgecolors='C1')
ax2.scatter(df4['n'][20], df4['p'][20], s=100, facecolors='none', edgecolors='C2')
ax2.set_xlabel(r'$n$')
ax2.legend(loc='best')

ax3.semilogy(df1['n'][:11], df1['p'][-11:],  label=r'$ESDIRK23$')
ax3.semilogy(df2['n'][:15], df2['p'][-15:],  label=r'$SDIRK33$')
ax3.semilogy(df4['n'][:21], df4['p'][-21:],  label=r'$ESDIRK35$')
ax3.set_xlabel(r'$n$')
ax3.legend(loc='best')

plt.tight_layout()
plt.savefig('res.png')
plt.close()
