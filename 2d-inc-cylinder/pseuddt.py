import matplotlib.pyplot as plt
import pandas as pd

def plot_residual(ax, df, y_cols, title, label):
    for col in y_cols:
        ax.semilogy(df['n'], df[col], label=col)
    ax.legend()
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Residual')
    ax.set_title(title)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')

fig, axes = plt.subplots(6, 1, figsize=(30, 30))

# Load data
# Load df1 only if it exists
try:
    lvl3 = pd.read_csv('/home/sambit/github/Improvements/PyFR-Test-Cases/2d-inc-cylinder/log-lvl3.csv')
    plot_residual(axes[0], lvl3[1::2], ['mean', 'min', 'max'], 'Residuals and Δτ mean vs pseudo-iterations', 'mean')
except:
    pass

try:
    lvl2 = pd.read_csv('/home/sambit/github/Improvements/PyFR-Test-Cases/2d-inc-cylinder/log-lvl2.csv')
    plot_residual(axes[1], lvl2[1::2], ['mean', 'min', 'max'], 'Residuals and Δτ mean vs pseudo-iterations', 'mean')
except:
    pass

try:
    lvl1 = pd.read_csv('/home/sambit/github/Improvements/PyFR-Test-Cases/2d-inc-cylinder/log-lvl1.csv')
    plot_residual(axes[2], lvl1[1::2], ['mean', 'min', 'max'], 'Residuals and Δτ mean vs pseudo-iterations', 'mean')
except:
    pass

try:
    lvl0 = pd.read_csv('/home/sambit/github/Improvements/PyFR-Test-Cases/2d-inc-cylinder/log-lvl0.csv')
    plot_residual(axes[3], lvl0[1::2], ['mean', 'min', 'max'], 'Residuals and Δτ mean vs pseudo-iterations', 'mean')
except:
    pass

df2 = pd.read_csv('/home/sambit/github/Improvements/PyFR-Test-Cases/2d-inc-cylinder/view_registers.csv').dropna()[:-5]

plot_residual(axes[-2], df2, ['p'], 'Residuals and Δτ mean vs pseudo-iterations', None)
plot_residual(axes[-1], df2, ['u'], 'Residuals and Δτ mean vs pseudo-iterations', None)

#for ax in axes.flatten():
#    ax.set_xlim(0, 1000)

# tight layout for all
plt.tight_layout()

plt.savefig('residual.png', dpi=400)
