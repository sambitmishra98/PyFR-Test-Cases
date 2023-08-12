# t,dt,cost,self.cost,err
# 0.00500,0.00500,590.06181,0.00000,0.58221
# 0.00995,0.00495,6.21820,590.06181,0.58220
# 0.01495,0.00500,4.38130,6.21820,0.58218
# 0.02000,0.00505,4.19781,4.38130,0.58216
# 0.02510,0.00510,4.18256,4.19781,0.58214
# 0.03025,0.00515,4.18783,4.18256,0.58213
# 0.03546,0.00520,4.12541,4.18783,0.58211
# 0.04071,0.00526,4.12398,4.12541,0.58209
# 0.04602,0.00531,4.01587,4.12398,0.58207
# 0.05138,0.00536,4.01631,4.01587,0.58206
# 0.05679,0.00541,4.03276,4.01631,0.58204
# 0.06226,0.00547,4.02344,4.03276,0.58202
# 0.06778,0.00552,3.90742,4.02344,0.58200
# 0.07336,0.00558,3.84439,3.90742,0.58198

# The above is in /home/sambit/github/Improvements/PyFR-Test-Cases/2d-inc-cylinder/terminal.csv
# Plot dt, cost, err with t

import matplotlib.pyplot as plt
import pandas as pd

# Read the data
df = pd.read_csv('dual_pi_controller.csv')

# Assuming there's no need to remove lines as before. 
# If needed, you can uncomment the following line.
df = df.iloc[30:]

t = df['t']
dt = df['dt']
cost = df['cost']
slope = df['slope']
err = df['err']

# Create the plots
fig, ax = plt.subplots(4, 1, sharex=True)

ax[0].plot(t, dt, label='dt')
ax[0].set_ylabel('dt')
ax[0].legend()

ax[1].semilogy(t, cost, label='cost', color='blue')
ax[1].set_ylabel('cost')
ax[1].legend()

ax[2].plot(t, slope, label='slope', color='blue')
ax[2].set_ylabel('slope')
ax[2].legend()

ax[3].plot(t, err, label='err')
ax[3].set_ylabel('err')
ax[3].legend()
ax[3].set_xlabel('t')

# Save the plot
plt.savefig('dual_pi_controller_plot.png', dpi=300)
