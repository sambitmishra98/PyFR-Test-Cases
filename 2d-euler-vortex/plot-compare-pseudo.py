import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#2x1
fig, ax = plt.subplots(2, 1, figsize=(10, 5))

df_come_im_int = pd.read_csv('compressible-implicit-int.csv')

df_come_im_psu = pd.read_csv('compressible-implicit-.csv')

ax[0].plot(df_come_im_int['t'], df_come_im_int['int-E'], label='compressible-implicit-PR1')
ax[0].set_xlabel('Time (s)')
ax[0].set_ylabel('Internal Energy (J)')
ax[0].legend()

ax[1].plot(df_come_im_psu['t'], df_come_im_psu['E'], label='compressible-implicit-PR1')
ax[1].set_xlabel('Time (s)')
ax[1].set_ylabel('Residual')
ax[1].legend()

plt.tight_layout()
plt.savefig('pseudo-res.png')
plt.close()
