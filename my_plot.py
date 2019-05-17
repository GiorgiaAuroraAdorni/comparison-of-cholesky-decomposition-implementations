import matplotlib.pyplot as plt


def plot_results(x, y, x_label, y_label, title):
    sorted_x, sorted_y = zip(*sorted(zip(x, y)))
    plt.plot(sorted_x, sorted_y, 'go-', linewidth=2, markersize=6)

    plt.xscale('log')
    plt.yscale('log')

    plt.xlabel(x_label, fontsize=6)
    plt.ylabel(y_label, fontsize=6)
    plt.title(title, weight='bold', fontsize=8)


def plot_comparison_result(x_set, y_set, x_label, y_label, labels, title):

    for i in range(len(x_set)):
        sorted_x, sorted_y = zip(*sorted(zip(x_set[i], y_set[i])))
        plt.plot(sorted_x, sorted_y, 'o-', linewidth=2, markersize=6, label=labels[i])

    plt.legend(loc='upper left')

    plt.xscale('log')
    plt.yscale('log')

    plt.xlabel(x_label, fontsize=6)
    plt.ylabel(y_label, fontsize=6)
    plt.title(title, weight='bold', fontsize=8)


def save_plot_os(columns, x, x_name, filename):
    # Plot based on the rows number of each matrix
    plt.subplots(nrows=3, ncols=1, figsize=(6, 8))

    plt.subplot(3, 1, 1)
    plot_results(columns[x], columns['solveTime'], x_name, 'Time (seconds)',
                 'Time required to solve the systems')

    plt.subplot(3, 1, 2)
    plot_results(columns[x], columns['relativeError'], x_name, 'Relative Error',
                 'Relative errors')

    plt.subplot(3, 1, 3)
    plot_results(columns[x], columns['maxMemory'], x_name, 'Max Memory (byte)',
                 'Max memory used to solve the systems')

    plt.tight_layout()
    plt.savefig(filename)
    plt.show()


def save_plot_comparison(columns, x, x_name, labels, filename):

    # Plot based on the rows number of each matrix
    plt.subplots(nrows=3, ncols=1, figsize=(6, 8))

    x_set = list()
    y_set1 = list()
    y_set2 = list()
    y_set3 = list()

    for i in range(len(columns)):
        x_set.append(columns[i][x])
        y_set1.append(columns[i]['solveTime'])
        y_set2.append(columns[i]['relativeError'])
        y_set3.append(columns[i]['maxMemory'])

    plt.subplot(3, 1, 1)
    plot_comparison_result(x_set, y_set1, x_name, 'Time (seconds)', labels, 'Time required to solve the systems')

    plt.subplot(3, 1, 2)
    plot_comparison_result(x_set, y_set2, x_name, 'Relative Error', labels, 'Relative errors')

    plt.subplot(3, 1, 3)
    plot_comparison_result(x_set, y_set3, x_name, 'Max Memory (byte)', labels, 'Max memory used to solve the systems')

    plt.tight_layout()
    plt.savefig(filename)
    plt.show()

