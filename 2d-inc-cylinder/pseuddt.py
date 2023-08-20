import matplotlib.pyplot as plt
import pandas as pd

def plot_residual(ax, df, y_cols, title, label):
    for col in y_cols:
        ax.semilogy(df['n'], df[col], label=col)
    ax.legend()
    ax.set_xlabel('Pseudo-time steps taken in the level (smoothing iterations in a cycle X number of cycles)')
    ax.set_title(title)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')

fig, axes = plt.subplots(6, 1, figsize=(15, 15))

# Load data
# Load df1 only if it exists
try:
    lvl3 = pd.read_csv('/home/sambit/github/Improvements/PyFR-Test-Cases/2d-inc-cylinder/log-lvl3.csv')
    plot_residual(axes[0], lvl3[1::2], ['mean', 'min', 'max'], 'Order 3 Δτ statistics with pseudo-iterations', 'mean')
except:
    pass

try:
    lvl2 = pd.read_csv('/home/sambit/github/Improvements/PyFR-Test-Cases/2d-inc-cylinder/log-lvl2.csv')
    plot_residual(axes[1], lvl2[1::2], ['mean', 'min', 'max'], 'Order 2 Δτ statistics with pseudo-iterations', 'mean')
except:
    pass

try:
    lvl1 = pd.read_csv('/home/sambit/github/Improvements/PyFR-Test-Cases/2d-inc-cylinder/log-lvl1.csv')
    plot_residual(axes[2], lvl1[1::2], ['mean', 'min', 'max'], 'Order 1 Δτ statistics with pseudo-iterations', 'mean')
except:
    pass

try:
    lvl0 = pd.read_csv('/home/sambit/github/Improvements/PyFR-Test-Cases/2d-inc-cylinder/log-lvl0.csv')
    plot_residual(axes[3], lvl0[1::2], ['mean', 'min', 'max'], 'Order 0 Δτ statistics with pseudo-iterations', 'mean')
except:
    pass

df2 = pd.read_csv('/home/sambit/github/Improvements/PyFR-Test-Cases/2d-inc-cylinder/view_registers.csv').dropna()[:-5]

plot_residual(axes[-2], df2, ['p'], 'Pressure L-2 norm of residual with pseudo-iterations', None)
plot_residual(axes[-1], df2, ['u'], 'U-velocity L-2 norm of residual with pseudo-iterations', None)

#for ax in axes.flatten():
#    ax.set_xlim(0, 1000)

# tight layout for all
plt.tight_layout()

plt.savefig('residual.png', dpi=200)
