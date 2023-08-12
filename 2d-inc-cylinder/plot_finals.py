import pandas as pd
import matplotlib.pyplot as plt

# Path to the CSV file
csv_path = "res_esdirk35_none.csv"

# Read the CSV file
df = pd.read_csv(csv_path)

# Drop duplicates for 't', keeping only the last entry
df_filtered = df.drop_duplicates(subset='t', keep='last')

# Plotting
fig, ax = plt.subplots(1, 1, figsize=(10, 5))

ax.plot(df_filtered['t'], df_filtered['p'], label='p', marker='o')
ax.plot(df_filtered['t'], df_filtered['u'], label='u', marker='x')
ax.plot(df_filtered['t'], df_filtered['v'], label='v', marker='s')

ax.set_xlabel('Time (t)')
ax.set_ylabel('Values')
ax.set_title('Final Entry Values of p, u, v for Each Unique t')
ax.legend(loc='best')
ax.grid(True, which="both", linestyle="--", linewidth=0.5)

plt.tight_layout()
plt.show()
