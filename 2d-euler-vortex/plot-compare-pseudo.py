import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig, ax = plt.subplots(1, 1, figsize=(10, 5))


df_come_im_dt  = pd.read_csv('pseudostats.csv')
df_come_im_dt2 = pd.read_csv('pseudostats_half-dt.csv')

ax.semilogy(df_come_im_dt['n'], df_come_im_dt['E'],  label=r'$\rho$')
ax.semilogy(df_come_im_dt2['n'], df_come_im_dt2['E'],  label=r'$\rho$', linestyle='--')

plt.tight_layout()
plt.savefig('pseudo-res.png')
plt.close()
