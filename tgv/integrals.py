import matplotlib.pyplot as plt
import pandas as pd

fig, (ax, ax2) = plt.subplots(1, 2, figsize=(6, 4))

df_ref = pd.read_csv('/home/sambit/github/Improvements/PyFR-Test-Cases/tgv/integral.csv')
# Plot the results
ax.plot(df_ref['t'], df_ref['int-E'], label='Reference')
ax2.plot(df_ref['t'], df_ref['int-enst'], label='Reference')

df = pd.read_csv('integral_implicit.csv')

ax.plot(df['t'], df['int-E'], label='Implicit')
ax.set_xlabel('Time')
ax.set_ylabel('Integral of E')
ax.legend()
ax.grid()
ax.set_xlim(0, 7)

ax2.plot(df['t'], df['int-enst'], label='Implicit')
ax2.set_xlabel('Time')
ax2.set_ylabel('Integral of enstrophy')
ax2.legend()
ax2.grid()
ax2.set_xlim(0, 7)


#save
plt.savefig('integrals.png', dpi=300, bbox_inches='tight')
