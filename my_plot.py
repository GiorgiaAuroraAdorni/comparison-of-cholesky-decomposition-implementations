import matplotlib.pyplot as plt


def plot_results(x, y, x_label, y_label, title):
    sorted_x, sorted_y = zip(*sorted(zip(x, y)))
    plt.plot(sorted_x, sorted_y, 'go-', linewidth=2, markersize=6)

    plt.xscale('log')
    plt.yscale('log')

    plt.xlabel(x_label, fontsize=6)
    plt.ylabel(y_label, fontsize=6)
    plt.title(title, weight='bold', fontsize=8)


def plot_comparison_result(x1, y1, x2, y2, x_label, y_label, title):
    sorted_x1, sorted_y1 = zip(*sorted(zip(x1, y1)))
    sorted_x2, sorted_y2 = zip(*sorted(zip(x2, y2)))

    plt.plot(sorted_x1, sorted_y1, 'go-', linewidth=2, markersize=6)
    plt.plot(sorted_x2, sorted_y2, 'oo-', linewidth=2, markersize=6)

    plt.xscale('log')
    plt.yscale('log')

    plt.xlabel(x_label, fontsize=6)
    plt.ylabel(y_label, fontsize=6)
    plt.title(title, weight='bold', fontsize=8)
    plt.legend(bbox_to_anchor=(0, 1), loc='upper left', ncol=1)


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


def save_plot_comparison(columns1, columns2, x1, x2, x_name, filename):

    # Plot based on the rows number of each matrix
    plt.subplots(nrows=3, ncols=1, figsize=(6, 8))

    plt.subplot(3, 1, 1)
    plot_comparison_result(columns1[x1], columns1['solveTime'], columns2[x2], columns2['solveTime'], x_name,
                           'Time (seconds)', 'Time required to solve the systems')

    plt.subplot(3, 1, 2)
    plot_comparison_result(columns1[x1], columns1['relativeError'], columns2[x2], columns2['solveTime'], x_name,
                           'Relative Error', 'Relative errors')

    plt.subplot(3, 1, 3)
    plot_comparison_result(columns1[x1], columns1['maxMemory'], columns2[x2], columns2['solveTime'], x_name,
                           'Max Memory (byte)', 'Max memory used to solve the systems')

    plt.tight_layout()
    plt.savefig(filename)
    plt.show()
