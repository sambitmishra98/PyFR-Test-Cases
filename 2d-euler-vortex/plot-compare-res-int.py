import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#2x1
fig, ax = plt.subplots(1, 2, figsize=(10, 5))

df_come_dv_int = pd.read_csv('compressible-explicit-dev-int.csv')
df_come_ex_int = pd.read_csv('compressible-explicit-int.csv')
df_come_im_int = pd.read_csv('compressible-implicit-int.csv')

df_come_dv_res = pd.read_csv('compressible-explicit-dev-res.csv')
df_come_ex_res = pd.read_csv('compressible-explicit-res.csv')
df_come_im_res = pd.read_csv('compressible-implicit-res.csv')

ax[0].plot(df_come_dv_int['t'], df_come_dv_int['int-E'], label='compressible-explicit-dev')
ax[0].plot(df_come_ex_int['t'], df_come_ex_int['int-E'], label='compressible-explicit-PR1')
ax[0].plot(df_come_im_int['t'], df_come_im_int['int-E'], label='compressible-implicit-PR1')
ax[0].set_xlabel('Time (s)')
ax[0].set_ylabel('Internal Energy (J)')
ax[0].legend()

ax[1].plot(df_come_dv_res['t'], df_come_dv_res['E'], label='compressible-explicit-dev')
ax[1].plot(df_come_ex_res['t'], df_come_ex_res['E'], label='compressible-explicit-PR1')
ax[1].plot(df_come_im_res['t'], df_come_im_res['E'], label='compressible-implicit-PR1')
ax[1].set_xlabel('Time (s)')
ax[1].set_ylabel('Residual')
ax[1].legend()

plt.tight_layout()
plt.savefig('compare.png')
plt.close()
