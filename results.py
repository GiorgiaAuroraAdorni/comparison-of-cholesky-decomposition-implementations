#!/usr/bin/env python3
from my_plot import save_plot_os, save_plot_comparison
from util import get_file, extract_columns

# Directories
# macos_out = get_file("macos", "matlabOutput.csv")
matlab_ubuntu = get_file("matlab/output/ubuntu", "matlabOutput.csv")
matlab_windows = get_file("matlab/output/windows", "matlabOutput.csv")

cpp_ubuntu_native_32 = get_file("cpp/output/ubuntu", "cppOutput-native-32.csv")
cpp_ubuntu_native_64 = get_file("cpp/output/ubuntu", "cppOutput-native-64.csv")
cpp_ubuntu_mkl = get_file("cpp/output/ubuntu", "cppOutput-mkl.csv")
cpp_windows_mkl = get_file("cpp/output/windows", "cppOutput-mkl.csv")
cpp_windows_native_64 = get_file("cpp/output/windows", "cppOutput-native-64.csv")

# columns_macos = extract_columns(macos_out)
columns_matlab_ubuntu = extract_columns(matlab_ubuntu)
columns_matlab_windows = extract_columns(matlab_windows)

columns_cpp_ubuntu_native_32 = extract_columns(cpp_ubuntu_native_32)
columns_cpp_ubuntu_native_64 = extract_columns(cpp_ubuntu_native_64)
columns_cpp_ubuntu_mkl = extract_columns(cpp_ubuntu_mkl)
columns_cpp_windows_mkl = extract_columns(cpp_windows_mkl)
columns_cpp_windows_native_64 = extract_columns(cpp_windows_native_64)

## Single plot
### NO
# save_plot_os(columns_macos, "rows", "Matrix Size", "results/macos_OnSize.pdf")
# save_plot_os(columns_macos, "nonZeros", "Non Zeros", "results/macos_OnNonZeros.pdf")
### NO

save_plot_os(columns_matlab_ubuntu, "rows", "Matrix Size", "results/single/matlab_ubuntu_OnSize.pdf")
save_plot_os(columns_matlab_ubuntu, "nonZeros", "Non Zeros", "results/single/matlab_ubuntu_OnNonZeros.pdf")

save_plot_os(columns_matlab_windows, "rows", "Matrix Size", "results/single/matlab_windows_OnSize.pdf")
save_plot_os(columns_matlab_windows, "nonZeros", "Non Zeros", "results/single/matlab_windows_OnNonZeros.pdf")

save_plot_os(columns_cpp_ubuntu_native_32, "rows", "Matrix Size", "results/single/cpp_ubuntu_native_32_OnSize.pdf")
save_plot_os(columns_cpp_ubuntu_native_32, "nonZeros", "Non Zeros", "results/single/cpp_ubuntu_native_32_OnNonZeros.pdf")

save_plot_os(columns_cpp_ubuntu_native_64, "rows", "Matrix Size", "results/single/cpp_ubuntu_native_64_OnSize.pdf")
save_plot_os(columns_cpp_ubuntu_native_64, "nonZeros", "Non Zeros", "results/single/cpp_ubuntu_native_64_OnNonZeros.pdf")

save_plot_os(columns_cpp_ubuntu_mkl, "rows", "Matrix Size", "results/single/cpp_ubuntu_mkl_OnSize.pdf")
save_plot_os(columns_cpp_ubuntu_mkl, "nonZeros", "Non Zeros", "results/single/cpp_ubuntu_mkl_OnNonZeros.pdf")

save_plot_os(columns_cpp_windows_mkl, "rows", "Matrix Size", "results/single/cpp_windows_mkl_OnSize.pdf")
save_plot_os(columns_cpp_windows_mkl, "nonZeros", "Non Zeros", "results/single/cpp_windows_mkl_OnNonZeros.pdf")

save_plot_os(columns_cpp_windows_native_64, "rows", "Matrix Size", "results/single/cpp_windows_native_64_OnSize.pdf")
save_plot_os(columns_cpp_windows_native_64, "nonZeros", "Non Zeros", "results/single/cpp_windows_native_64_OnNonZeros.pdf")

## Comparison between the matlab plot in windows and ubuntu
save_plot_comparison([columns_matlab_ubuntu, columns_matlab_windows], "rows", "Matrix Size",
                     ["matlab ubuntu", "matlab windows"], "results/comparison/matlab_ubuntu_windows_OnSize.pdf")
save_plot_comparison([columns_matlab_ubuntu, columns_matlab_windows], "nonZeros", "Non Zeros", ["matlab ubuntu",
                     "matlab windows"], "results/comparison/matlab_ubuntu_windows_OnNonZeros.pdf")

save_plot_comparison([columns_cpp_ubuntu_mkl, columns_cpp_windows_mkl], "rows", "Matrix Size", ["cpp mkl ubuntu",
                     "cpp mkl windows"], "results/comparison/cpp_mkl_ubuntu_windows_OnSize.pdf")
save_plot_comparison([columns_cpp_ubuntu_mkl, columns_cpp_windows_mkl], "nonZeros", "Non Zeros", ["cpp mkl ubuntu",
                     "cpp mkl windows"], "results/comparison/cpp_mkl_ubuntu_windows_OnNonZeros.pdf")

save_plot_comparison([columns_cpp_ubuntu_native_64, columns_cpp_ubuntu_native_32], "rows", "Matrix Size",
                     ["cpp native 64 ubuntu", "cpp native 32 ubuntu"], "results/comparison/cpp_native_64_32_ubuntu_OnSize.pdf")
save_plot_comparison([columns_cpp_ubuntu_native_64, columns_cpp_ubuntu_native_32], "nonZeros", "Non Zeros",
                     ["cpp native 64 ubuntu", "cpp native 32 ubuntu"], "results/comparison/cpp_native_64_32_ubuntu_OnNonZeros.pdf")

save_plot_comparison([columns_cpp_ubuntu_native_64, columns_cpp_ubuntu_mkl], "rows", "Matrix Size",
                     ["cpp native 64 ubuntu", "cpp mkl ubuntu"], "results/comparison/cpp_native_64_mkl_ubuntu_OnSize.pdf")
save_plot_comparison([columns_cpp_ubuntu_native_64, columns_cpp_ubuntu_mkl], "nonZeros", "Non Zeros",
                     ["cpp native 64 ubuntu", "cpp mkl ubuntu"], "results/comparison/cpp_native_64_mkl_ubuntu_OnNonZeros.pdf")

save_plot_comparison([columns_cpp_windows_native_64, columns_cpp_windows_mkl], "rows", "Matrix Size",
                     ["cpp native 64 windows", "cpp mkl windows"], "results/comparison/cpp_native_64_mkl_windows_OnSize.pdf")
save_plot_comparison([columns_cpp_windows_native_64, columns_cpp_windows_mkl], "nonZeros", "Non Zeros",
                     ["cpp native 64 windows", "cpp mkl windows"], "results/comparison/cpp_native_64_mkl_windows_OnNonZeros.pdf")

save_plot_comparison([columns_cpp_ubuntu_native_64, columns_cpp_windows_native_64], "rows", "Matrix Size",
                     ["cpp native 64 ubuntu", "cpp windows native 64"], "results/comparison/cpp_native_64_ubuntu_windows_OnSize.pdf")
save_plot_comparison([columns_cpp_ubuntu_native_64, columns_cpp_windows_native_64], "nonZeros", "Non Zeros",
                     ["cpp native 64 ubuntu", "cpp windows native 64"], "results/comparison/cpp_native_64_ubuntu_windows_OnNonZeros.pdf")

save_plot_comparison([columns_cpp_ubuntu_native_64, columns_cpp_ubuntu_mkl, columns_matlab_ubuntu], "rows", "Matrix Size",
                     ["cpp native 64 ubuntu", "cpp mkl ubuntu", "matlab ubuntu"], "results/comparison/all_ubuntu_OnSize.pdf")
save_plot_comparison([columns_cpp_ubuntu_native_64, columns_cpp_ubuntu_mkl, columns_matlab_ubuntu], "nonZeros", "Non Zeros",
                     ["cpp native 64 ubuntu", "cpp mkl ubuntu", "matlab ubuntu"], "results/comparison/all_ubuntu_OnNonZeros.pdf")

save_plot_comparison([columns_cpp_windows_native_64, columns_cpp_windows_mkl, columns_matlab_windows], "rows", "Matrix Size",
                     ["cpp native 64 windows", "cpp mkl windows", "matlab windows"], "results/comparison/all_windows_OnSize.pdf")
save_plot_comparison([columns_cpp_windows_native_64, columns_cpp_windows_mkl, columns_matlab_windows], "nonZeros", "Non Zeros",
                     ["cpp native 64 windows", "cpp mkl windows", "matlab windows"], "results/comparison/all_windows_OnNonZeros.pdf")
