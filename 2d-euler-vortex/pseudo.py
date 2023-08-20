import matplotlib.pyplot as plt
import pandas as pd

def plot_residual(ax, df, y_cols, title):
    for col in y_cols:
        ax.semilogy(df['n'], df[col], label=col)
    ax.legend()
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Residual')
    ax.set_title(title)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')

fig, axes = plt.subplots(3, 1, figsize=(15, 15), sharex=True)

# Load data
# Load df1 only if it exists
try:
    lvl4 = pd.read_csv('/home/sambit/github/Improvements/PyFR-Test-Cases/tgv/log-lvl4.csv')
    plot_residual(axes[0], lvl4[1::2], ['mean', 'min', 'max'], 'Residuals and Δτ mean vs pseudo-iterations')
except:
    pass

#try:
#    lvl2 = pd.read_csv('/home/sambit/github/Improvements/PyFR-Test-Cases/tgv/log-lvl2.csv')
#    plot_residual(axes[1], lvl2[1::2], ['mean', 'min', 'max'], 'Residuals and Δτ mean vs pseudo-iterations', 'mean')
#except:
#    pass
#
#try:
#    lvl1 = pd.read_csv('/home/sambit/github/Improvements/PyFR-Test-Cases/tgv/log-lvl1.csv')
#    plot_residual(axes[2], lvl1[1::2], ['mean', 'min', 'max'], 'Residuals and Δτ mean vs pseudo-iterations', 'mean')
#except:
#    pass
#
#try:
#    lvl0 = pd.read_csv('/home/sambit/github/Improvements/PyFR-Test-Cases/tgv/log-lvl0.csv')
#    plot_residual(axes[3], lvl0[1::2], ['mean', 'min', 'max'], 'Residuals and Δτ mean vs pseudo-iterations', 'mean')
#except:
#    pass
#

try:
    df2 = pd.read_csv('/home/sambit/github/Improvements/PyFR-Test-Cases/tgv/residuals_acm.csv').dropna()[:-5]
    plot_residual(axes[-2], df2, ['p'], 'Residuals ')
    plot_residual(axes[-1], df2, ['u'], 'Residuals ')
except:
    pass

#for ax in axes.flatten():
#    ax.set_xlim(0, 1000)

# tight layout for all
plt.tight_layout()

plt.savefig('residual.png', dpi=200)
