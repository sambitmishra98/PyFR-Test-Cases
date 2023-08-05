import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file
df = pd.read_csv('test_96.csv')
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 6))

x = np.linspace(0.00025, 0.00075, 100)
ax1.semilogy(df['n'], df['performance'], label='performance')
ax1.set_ylabel('performance')
ax1.legend()
ax1.set_xlim(right=10)

x = np.linspace(0.00025, 0.00075, 100)
ax2.semilogy(df['n'], df['mean'], label='mean')
ax2.set_ylabel('mean')
ax2.legend()

# Get a standard error in mean of the performance over an expanding window
ax3.semilogy(df['n'], df['rel-err'], label='rem')
ax3.set_xlabel('t')
ax3.set_ylabel('rem')
ax3.legend()
plt.savefig('test_96.png')