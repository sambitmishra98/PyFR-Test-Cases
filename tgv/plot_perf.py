import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file
df = pd.read_csv('benchmark.csv')
df = df.iloc[10:]
df['performance_avg'] = df['performance'].rolling(100).mean()

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))

x = np.linspace(0.00025, 0.00075, 100)
ax1.semilogy(df['t'], df['performance'], label='performance')
ax1.semilogy(df['t'], df['performance_avg'], label='performance_avg')
ax1.set_ylabel('performance')
ax1.legend()

# Get a standard error in mean of the performance over an expanding window
df['performance_sem'] = df['performance'].expanding().apply(lambda x: x.sem()) / df['performance_avg']
ax2.semilogy(df['t'], df['performance_sem'], label='performance_sem')
ax2.set_xlabel('t')
ax2.set_ylabel('performance_sem')
ax2.legend()
plt.savefig('benchmark_performance.png')