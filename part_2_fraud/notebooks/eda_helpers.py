import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from matplotlib.ticker import FuncFormatter
from matplotlib.ticker import ScalarFormatter
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

def plotStrip(x, y, hue, figsize = (14, 9)):
    
    fig = plt.figure(figsize = figsize)
    plt.yscale('linear')
    colours = plt.cm.tab10(np.linspace(0, 1, 9))
    with sns.axes_style('ticks'):
        ax = sns.stripplot(x, y, \
             hue = hue, jitter = 0.4, marker = '.', \
             size = 4, palette = colours)
        plt.yscale('linear')
        ax.set_xlabel('')
        ax.set_xticklabels(['genuine', 'fraudulent'], size = 16)
        ax.set_yscale("linear")
        for axis in ['top','bottom','left','right']:
            ax.spines[axis].set_linewidth(2)

        handles, labels = ax.get_legend_handles_labels()
        plt.legend(handles, ['Transfer', 'Cash out'], bbox_to_anchor=(1, 1), \
               loc=2, borderaxespad=0, fontsize = 16);
    ax = plt.gca()
    ax.yaxis.set_minor_formatter(FuncFormatter(lambda y, pos: f"{y:,.0f}"))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda y, pos: f"{y:,.0f}"))
    return ax