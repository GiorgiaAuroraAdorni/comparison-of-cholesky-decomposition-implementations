#!/usr/bin/env python3
from my_plot import save_plot_os, save_plot_comparison
from util import get_file, extract_columns
import os

os.chdir("matlab/output")

macos_out = get_file("macos", "matlabOutput.csv")
ubuntu_out = get_file("ubuntu", "matlabOutput.csv")
windows_out = get_file("windows", "matlabOutput.csv")

columns_macos = extract_columns(macos_out)
columns_ubuntu = extract_columns(ubuntu_out)
columns_windows = extract_columns(windows_out)

##
save_plot_os(columns_macos, "rows", "Matrix Size", "results/macos_OnSize.pdf")
save_plot_os(columns_macos, "nonZeros", "Non Zeros", "results/macos_OnNonZeros.pdf")

save_plot_os(columns_ubuntu, "rows", "Matrix Size", "results/ubuntu_OnSize.pdf")
save_plot_os(columns_ubuntu, "nonZeros", "Non Zeros", "results/ubuntu_OnNonZeros.pdf")

save_plot_os(columns_windows, "rows", "Matrix Size", "results/windows_OnSize.pdf")
save_plot_os(columns_windows, "nonZeros", "Non Zeros", "results/windows_OnNonZeros.pdf")

##
save_plot_comparison(columns_ubuntu, columns_windows, "rows", "Matrix Size", "results/ubuntu-windows_comparisonOnSize.pdf")
save_plot_comparison(columns_ubuntu, columns_windows, "nonZeros", "Non Zeros", "results/ubuntu-windows_comparisonOnNonZeros.pdf")
