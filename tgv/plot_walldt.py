import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import lognorm
import numpy as np

# Read the CSV file
df = pd.read_csv('benchmark.csv')
df = df.iloc[3:]
df['walldt_avg'] = df['walldt'].rolling(1000).mean()
params = lognorm.fit(df['walldt'])

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))

x = np.linspace(0.00025, 0.00075, 100)
pdf_fitted = lognorm.pdf(x, params[0], loc=params[1], scale=params[2])
ax1.semilogy(df['t'], df['walldt'], label='walldt')
ax1.semilogy(df['t'], df['walldt_avg'], label='walldt_avg')
ax1.set_ylabel('walldt')
ax1.legend()
ax2.hist(df['walldt'], bins=1000, density=True, label='walldt')
ax2.plot(x, pdf_fitted, 'r-', label='lognormal fit')
ax2.set_xlabel('t')
ax2.set_ylabel('pdf')
ax2.legend()
plt.savefig('benchmark_combined.png')
