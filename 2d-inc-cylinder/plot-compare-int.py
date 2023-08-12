import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig, ax = plt.subplots(1, 1, figsize=(5, 3))


df2  = pd.read_csv('int_sdirk33_none_pi.csv')
df4  = pd.read_csv('int_esdirk35_none_pi.csv')
df5  = pd.read_csv('int_esdirk35_pi_pi.csv')

ax.plot(df2['t'], df2['int-E'], label=r'$SDIRK33$', linewidth=2)
ax.plot(df4['t'], df4['int-E'], label=r'$ESDIRK35-none$', linewidth=2)
ax.plot(df5['t'], df5['int-E'], label=r'$ESDIRK35-pi$', linewidth=2)

ax.set_xlabel(r'$n$')
ax.legend(loc='best')

plt.tight_layout()
plt.savefig('int_localpi.png', dpi=300)
plt.close()
