import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np


def plot_results(x, y, x_label, y_label, title):
    sorted_x, sorted_y = zip(*sorted(zip(x, y)))
    plt.plot(sorted_x, sorted_y, 'go-', linewidth=2, markersize=6)

    plt.xscale('log')
    plt.yscale('log')

    plt.xlabel(x_label, fontsize=12)
    plt.ylabel(y_label, fontsize=12)
    plt.title(title, weight='bold', fontsize=14)


def plot_comparison_result(x_set, y_set, x_label, y_label, labels, title):

    for i in range(len(x_set)):
        sorted_x, sorted_y = zip(*sorted(zip(x_set[i], y_set[i])))

        if i == 0:
            plt.plot(sorted_x, sorted_y, color='#1F77B4', marker='o', linestyle='-', linewidth=3, markersize=8, label=labels[i])
        elif i==1:
            plt.plot(sorted_x, sorted_y, color='#FF7F0D', marker='o', linestyle='-', linewidth=3, markersize=8, label=labels[i])
        elif i==2:
            plt.plot(sorted_x, sorted_y, color='#2DA02C', marker='o', linestyle='-', linewidth=3, markersize=8, label=labels[i])
        elif i==3:
            plt.plot(sorted_x, sorted_y, color='#1F77B4', marker='o', linestyle='--', linewidth=3, markersize=8, label=labels[i])
        elif i==4:
            plt.plot(sorted_x, sorted_y, color='#FF7F0D', marker='o', linestyle='--', linewidth=3, markersize=8, label=labels[i])
        else:
            plt.plot(sorted_x, sorted_y, color='#2DA02C', marker='o', linestyle='--', linewidth=3, markersize=8, label=labels[i])

    plt.xscale('log')
    plt.yscale('log')

    plt.xlabel(x_label, fontsize=12)
    plt.ylabel(y_label, fontsize=12)

    # for i in zip(x_set[0], y_set[0], annotations[0]):
    #     plt.annotate(i[2],
    #                  xy=(i[0], min(y_set[0])),
    #                  xytext=(0, -50),
    #                  xycoords='data',
    #                  textcoords="offset points",
    #                  rotation="vertical")

    #locs, labels = plt.xticks()
    #plt.xticks(locs, clip_on=False)
    # minimum_exp = round(np.math.log10(min(x_set[1]))) - 1
    # maximum_exp = round(np.math.log10(max(x_set[1]))) + 1

    # f = mticker.ScalarFormatter(useOffset=False, useMathText=True)
    # g = lambda x, pos: "${}$".format(f._formatSciNotation('%1.10e' % x))
    # fmt = mticker.FuncFormatter(g)

    # locs = np.concatenate([x_set[1], [10 ** minimum_exp, 10 ** maximum_exp]])
    # labels = np.concatenate([annotations[1], [str(fmt(10 ** minimum_exp)), str(fmt(10 ** maximum_exp))]])
    # plt.xticks(locs, labels, fontsize=6, rotation="vertical")

    plt.title(title, weight='bold', fontsize=14, y=1.05)


def save_plot_os(columns, x, x_name, filename):
    # Plot based on the rows number of each matrix
    plt.subplots(nrows=1, ncols=3, figsize=(24, 6))

    plt.subplot(1, 3, 1)
    plot_results(columns[x], columns['solveTime'], x_name, 'Time (seconds)',
                 'Time required to solve the systems')

    plt.subplot(1, 3, 2)
    plot_results(columns[x], columns['relativeError'], x_name, 'Relative Error',
                 'Relative errors')

    plt.subplot(1, 3, 3)
    plot_results(columns[x], columns['maxMemory'], x_name, 'Max Memory (byte)',
                 'Max memory used to solve the systems')

    plt.tight_layout()
    plt.savefig(filename)
    plt.show()


def save_plot_comparison(columns, x, x_name, labels, filename):

    # Plot based on the rows number of each matrix
    plt.subplots(nrows=1, ncols=1, figsize=(24, 6))

    x_set = list()
    y_set1 = list()
    y_set2 = list()
    y_set3 = list()
    annotations = list()

    for i in range(len(columns)):
        x_set.append(columns[i][x])
        y_set1.append(columns[i]['solveTime'])
        y_set2.append(columns[i]['relativeError'])
        y_set3.append(columns[i]['maxMemory'])
        names = [name.replace(".mtx", "").replace(".gz", "") for name in columns[i]["name"]]
        annotations.append(names)

    plt.subplot(1, 3, 1)
    plt.subplots_adjust(left=0.05, bottom=0.2, right=0.95, top=0.85, wspace=None, hspace=None)
    plot_comparison_result(x_set, y_set1, x_name, 'Time (seconds)', labels, 'Time required to solve the systems')
    
    plt.figlegend(loc="lower center", ncol=6, labelspacing=0.)

    plt.subplot(1, 3, 2)
    plt.subplots_adjust(left=0.05, bottom=0.2, right=0.95, top=0.85, wspace=None, hspace=None)
    plot_comparison_result(x_set, y_set2, x_name, 'Relative Error', labels, 'Relative errors')
    
    plt.subplot(1, 3, 3)
    plt.subplots_adjust(left=0.05, bottom=0.2, right=0.95, top=0.85, wspace=None, hspace=None)
    plot_comparison_result(x_set, y_set3, x_name, 'Max Memory (byte)', labels, 'Max memory used to solve the systems')
    

    #plt.tight_layout()
    plt.savefig(filename)
    plt.show()

