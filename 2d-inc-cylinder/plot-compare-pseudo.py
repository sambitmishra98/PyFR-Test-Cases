import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig, (ax, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 5))


df11  = pd.read_csv('res_esdirk23_none.csv')
df12  = pd.read_csv('res_esdirk23_pi.csv')
df2  = pd.read_csv('res_sdirk33.csv')

# Plot only the fifth entry

ax.semilogy(df11['t'][10::11], df11['p'][10::11],  label=r'$ESDIRK35$')
ax.semilogy(df12['t'][10::11], df12['p'][10::11],  label=r'$ESDIRK35$')
ax.semilogy(df2['t'][::15]  , df2['p'][::15],  label=r'$SDIRK33$')

ax.set_xlabel(r'$t$')

ax2.semilogy(df11['n'][:11], df11['p'][:11],  label=r'$ESDIRK23$')
ax2.semilogy(df12['n'][:11], df12['p'][:11],  label=r'$ESDIRK23$')
ax2.semilogy(df2['n'][:15], df2['p'][:15],  label=r'$SDIRK33$')
ax2.scatter(df11['n'][10], df11['p'][10], s=100, facecolors='none', edgecolors='C0')
ax2.scatter(df12['n'][10], df12['p'][10], s=100, facecolors='none', edgecolors='C0')
ax2.scatter(df2['n'][14], df2['p'][14], s=100, facecolors='none', edgecolors='C1')
ax2.set_xlabel(r'$n$')
ax2.legend(loc='best')

ax3.semilogy(df11['n'][:11], df11['p'][-11:],  label=r'$ESDIRK23$')
ax3.semilogy(df12['n'][:11], df12['p'][-11:],  label=r'$ESDIRK23$')
ax3.semilogy(df2['n'][:15], df2['p'][-15:],  label=r'$SDIRK33$')
ax3.set_xlabel(r'$n$')
ax3.legend(loc='best')

plt.tight_layout()
plt.savefig('res.png')
plt.close()
