import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig, (ax, ax2) = plt.subplots(2, 1, figsize=(10, 5))


df1  = pd.read_csv('esdirk23-pseudostats.csv')
df2  = pd.read_csv('sdirk33-pseudostats.csv')
df3  = pd.read_csv('sdirk43-pseudostats.csv')
df4  = pd.read_csv('esdirk35-pseudostats.csv')

# Plot only the fifth entry

ax.semilogy(df2['t'][::15], df2['E'][::15],  label=r'$SDIRK33$')
ax.semilogy(df3['t'][::15], df3['E'][::15],  label=r'$SDIRK43$')
ax.semilogy(df1['t'][10::11], df1['E'][10::11],  label=r'$ESDIRK23$')
ax.semilogy(df4['t'][20::21], df4['E'][20::21],  label=r'$ESDIRK35$')

ax.set_xlabel(r'$t$')

ax2.semilogy(df2['n'][:15], df2['E'][:15],  label=r'$SDIRK33$')
ax2.semilogy(df3['n'][:15], df3['E'][:15],  label=r'$SDIRK43$')
ax2.semilogy(df1['n'][:11], df1['E'][:11],  label=r'$ESDIRK23$')
ax2.semilogy(df4['n'][:21], df4['E'][:21],  label=r'$ESDIRK35$')

# circle the last point with the same color as the line
ax2.scatter(df2['n'][14], df2['E'][14], s=100, facecolors='none', edgecolors='C0')
ax2.scatter(df3['n'][14], df3['E'][14], s=100, facecolors='none', edgecolors='C1')
ax2.scatter(df1['n'][10], df1['E'][10], s=100, facecolors='none', edgecolors='C2')
ax2.scatter(df4['n'][20], df4['E'][20], s=100, facecolors='none', edgecolors='C3')




ax2.set_xlabel(r'$n$')
ax2.legend(loc='best')

plt.tight_layout()
plt.savefig('pseudo-res.png')
plt.close()
