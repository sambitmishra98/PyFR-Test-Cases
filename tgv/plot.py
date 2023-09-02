import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
# Replace 'your_data.csv' with the path to your actual CSV file
df = pd.read_csv('dual_pi_controller.csv')

# Get the names of all columns except the first one ('t')
columns_to_plot = df.columns[1:]

# Create subplots
fig, axs = plt.subplots(len(columns_to_plot), 1, figsize=(10, 15), sharex=True)

# Loop through each column to plot
for i, col in enumerate(columns_to_plot):
    axs[i].plot(df['t'], df[col])
    axs[i].set_title(f'{col} vs t')
    axs[i].set_xlabel('t')
    axs[i].set_ylabel(col)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plots
plt.savefig('dual_pi_controller.png')
plt.show()
