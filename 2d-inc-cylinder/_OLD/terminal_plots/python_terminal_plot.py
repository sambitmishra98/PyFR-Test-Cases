# t,dt,cost,past_cost,err
# 75.50000,   0.50000, 42.54219,0.00000,    0.40448
# 75.99505,   0.49505, 1.99869, 42.54219,   0.40308
# 76.49505,   0.50000, 1.87423, 1.99869,    0.40222
# 77.00005,   0.50500, 1.85830, 1.87423,    0.40186
# 77.51010,   0.51005, 1.82805, 1.85830,    0.40196
# 78.02525,   0.51515, 1.82279, 1.82805,    0.40231
# 78.54555,   0.52030, 1.80313, 1.82279,    0.40275
# 79.07106,   0.52551, 1.80416, 1.80313,    0.40336
# 79.60182,   0.53076, 1.86424, 1.80416,    0.40461
# 80.12732,   0.52551, 1.78835, 1.86424,    0.40544
# 80.65808,   0.53076, 1.72821, 1.78835,    0.40383
# 81.19415,   0.53607, 1.70944, 1.72821,    0.40276
# 81.73558,   0.54143, 1.68916, 1.70944,    0.40217
# 82.28242,   0.54684, 1.75088, 1.68916,    0.40193


# The above is in /home/sambit/github/Improvements/PyFR-Test-Cases/2d-inc-cylinder/terminal.csv
# Plot dt, cost, err with t

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('terminal.csv')

# Remove the first line
df = df.iloc[2:]

t = df['t']
dt = df['dt']
cost = df['cost']
past_cost = df['past_cost']
err = df['err']

fig, ax = plt.subplots(3,1, sharex=True)

ax[0].plot(t, dt, label='dt')
ax[0].set_ylabel('dt')
ax[0].legend()

ax[1].plot(t, cost, label='cost')
ax[1].set_ylabel('cost')
ax[1].legend()

ax[2].plot(t, err, label='err')
ax[2].set_ylabel('err')
ax[2].legend()

ax[2].set_xlabel('t')

plt.savefig('terminal.png', dpi=300)

