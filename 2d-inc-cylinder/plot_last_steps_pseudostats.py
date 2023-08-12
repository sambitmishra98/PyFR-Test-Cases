# /home/sambit/github/Improvements/PyFR-Test-Cases/2d-inc-cylinder/res_esdirk35_pi_pi.csv
# pseudo-steps,tcurr,n,res,res_p,res_u,res_v,min,min_p,min_p_quad,min_p_tri,min_u,min_u_quad,min_u_tri,min_v,min_v_quad,min_v_tri,max,max_p,max_p_quad,max_p_tri,max_u,max_u_quad,max_u_tri,max_v,max_v_quad,max_v_tri
# 68,75.5,68,0.002005141561302284,0.0018409173659853324,5.569224879285041e-05,0.00010853194652410093,0.0029856657919694633,0.0029856657919694633,0.0029856657919694633,0.0029856657919694633,0.006,0.006,0.006,0.006,0.006,0.006,0.006,0.006,0.006,0.006,0.006,0.006,0.006,0.006,0.006,0.006
# 128,75.9950495049505,60,0.002034169496554852,0.001855987924579492,6.360691560146497e-05,0.00011457465637389505,0.0026331558605646936,0.0026331558605646936,0.0026331558605646936,0.0026331558605646936,0.005940594059405941,0.005940594059405941,0.005940594059405941,0.005940594059405941,0.005940594059405941,0.005940594059405941,0.005940594059405941,0.005940594059405941,0.005940594059405941,0.005940594059405941,0.005940594059405941,0.005940594059405941,0.005940594059405941,0.005940594059405941,0.005940594059405941,0.005940594059405941
# 188,76.4950495049505,60,0.0021180560760304186,0.001936057339565867,6.645324393190717e-05,0.00011554549253264416,0.0026963291825423024,0.0026963291825423024,0.0026963291825423024,0.0026963291825423024,0.006,0.006,0.006,0.006,0.006,0.006,0.006,0.006,0.006,0.006,0.006,0.006,0.006,0.006,0.006,0.006

import pandas as pd
import matplotlib.pyplot as plt


def load_data(path):
    return pd.read_csv(path)


def plot_data(ax, x_data, y_data, labels, ylabel, logscale=True):
    for y, label in zip(y_data, labels):
        if y.isnull().all():  # If the entire series is NaN, skip plotting it
            continue
        if logscale:
            ax.semilogy(x_data, y, label=label)
        else:
            ax.plot(x_data, y, label=label)
    ax.set_ylabel(ylabel)
    ax.grid(True)
    if ax.get_legend_handles_labels()[0]:  # Only add legend if there are handles
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)


def main():
    # Load Data
    dataset = load_data('/home/sambit/github/Improvements/PyFR-Test-Cases/2d-inc-cylinder/pseudodt_esdirk35_pi_pi_more.csv')

    # Plotting Configuration
    fig, ax = plt.subplots(4, 1, sharex=True, sharey=True, figsize=(10, 10))
    
    plots_config = [
        {
            'y_data': [dataset['min_p'], dataset['min_u'], dataset['min_v'], dataset['max_p'], dataset['max_u'], dataset['max_v']],
            'labels': ['min-p', 'min-u', 'min-v', 'max-p', 'max-u', 'max-v'],
            'ylabel': 'Min/Max Δτ'
        },
        {
            'y_data': [dataset['min_p_quad'], dataset['min_p_tri'], dataset['max_p_quad'], dataset['max_p_tri']],
            'labels': ['min-quad', 'min-tri', 'max-quad', 'max-tri'],
            'ylabel': 'Min/Max Δτ pressure'
        },
        {
            'y_data': [dataset['min_u_quad'], dataset['min_v_quad'], dataset['min_u_tri'], dataset['min_v_tri']],
            'labels': ['u-quad', 'v-quad', 'u-tri', 'v-tri'],
            'ylabel': 'Min Δτ velocity'
        },
        {
            'y_data': [dataset['max_u_quad'], dataset['max_v_quad'], dataset['max_u_tri'], dataset['max_v_tri']],
            'labels': ['u-quad', 'v-quad', 'u-tri', 'v-tri'],
            'ylabel': 'Max Δτ velocity'
        }
    ]

    # Plot data
    for axis, config in zip(ax, plots_config):
        plot_data(axis, dataset['pseudo-steps'], config['y_data'], config['labels'], config['ylabel'])

    # Draw a horizontal line at y = 2e-2 for reference
    for axis in ax:
        axis.axhline(y=2e-2, color='k', linestyle='--')

    
    ax[-1].set_xlabel('pseudo-steps')
    plt.tight_layout()
    plt.savefig('p_u_v_vs_n_more_LVL3.png', dpi=300)


if __name__ == "__main__":
    main()
