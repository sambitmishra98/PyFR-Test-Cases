import os
import matplotlib.pyplot as plt
import pandas as pd

BASE_PATH = '/home/sambit/github/Improvements/PyFR-Test-Cases/tgv'

def plot_Δτ(ax, df, var, title):
    """
    Plot Δτ values.
    
    Parameters:
    - ax: The axis to plot on.
    - df: The dataframe containing the data.
    - var: The variable to plot (e.g., 'p' or 'u').
    - title: The title for the plot.
    """
    ax.semilogy(df['n'], df[f'mean-{var}'], label=f'Δτ-{var}')
    ax.fill_between(df['n'], df[f'min-{var}'], df[f'max-{var}'], alpha=0.2)
    ax.set_yscale('log')
    ax.legend()
    ax.set_title(title)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')

def plot_residual(ax, df, var, title):
    """
    Plot residual values.
    
    Parameters are the same as plot_Δτ.
    """
    ax.semilogy(df['n'], df[f'l2-{var}'], label=f'l2-{var}')
    ax.semilogy(df['n'], df[f'max-{var}'], label=f'max-{var}', linestyle='--')
    ax.legend()
    ax.set_title(title)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')

fig, axes = plt.subplots(5, 2, figsize=(30, 20), sharex=True, sharey=True)

for i in range(5):
    dtau_path = os.path.join(BASE_PATH, f'dtau-lvl{i}.csv')
    res_path = os.path.join(BASE_PATH, f'res-lvl{i}.csv')
    
    try:
        lvl4 = pd.read_csv(dtau_path)
        plot_Δτ(axes[4-i][0], lvl4[1::2], 'p', f'Level {i}')
        plot_Δτ(axes[4-i][1], lvl4[1::2], 'u', f'Level {i}')
    except FileNotFoundError:
        pass

    try:
        df2 = pd.read_csv(res_path)
        plot_residual(axes[4-i][0], df2, 'p', f'Level {i}')
        plot_residual(axes[4-i][1], df2, 'u', f'Level {i}')
    except FileNotFoundError:
        pass

plt.tight_layout()
plt.savefig('residual.png', dpi=300)
