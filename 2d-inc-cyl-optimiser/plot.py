import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('data.csv')  # Replace 'your_file.csv' with the actual file name

# Plotting
fig, axes = plt.subplots(3, figsize=(12, 8), sharex=True, sharey=True)

for j, ax in zip(['p','u','v'], axes):
    for i in range(4):
        ax.semilogy(df['iter'], df[f'm{i}-{j}'], label=f'modal residual for {j} at level {i}')
    ax.legend()
    ax.set_xlabel('Cycle iterations')
    ax.set_ylabel(f'Modal residuals for {j}')

# Set xlimits from 5000 to 5100
# axes[0].set_xlim(5000, 5100)

# Show the plot and also save it as a PNG image
plt.tight_layout()
plt.savefig('plot.png')
plt.show()