#include "utils/MatrixMarket.h"

#include <Eigen/Eigen>

#include <boost/algorithm/string.hpp>
#include <boost/filesystem.hpp>

#include <chrono>
#include <iostream>

struct MatrixInfo {
    Eigen::Index rows;
    Eigen::Index nonZeros;

    double relativeError;

    std::chrono::duration<double> loadTime;
    std::chrono::duration<double> solveTime;
};

template<typename SparseMatrixType>
Eigen::VectorXd solveSystem(SparseMatrixType A, Eigen::VectorXd b) {
    using namespace Eigen;

    SimplicialLDLT<SparseMatrix<double>> solver(A);

    return solver.solve(b);
}

MatrixInfo processMatrix(const std::string &filename) {
    using namespace Eigen;

    MatrixInfo info;
    SparseMatrix<double> A;

    {
        std::cerr << "Loading matrix '" << filename << "'... " << std::flush;

        auto start = std::chrono::high_resolution_clock::now();

        SparseMatrix<double> matrix;
        bool result = loadMarketGzip(matrix, filename);

        A = matrix.selfadjointView<Lower>();

        auto end = std::chrono::high_resolution_clock::now();

        std::cerr << (result ? "OK" : "ERROR") << std::endl;

        info.rows = A.rows();
        info.nonZeros = A.nonZeros();
        info.loadTime = end - start;

        std::cerr << "Rows: " << info.rows << std::endl;
        std::cerr << "Non-zero elements: " << info.nonZeros << std::endl;
    }

    {
        VectorXd xe = VectorXd::Ones(A.rows());
        VectorXd b = A * xe;

        std::cerr << "Solving system... " << std::flush;

        auto start = std::chrono::high_resolution_clock::now();

        VectorXd x = solveSystem(A, b);

        auto end = std::chrono::high_resolution_clock::now();

        std::cerr << "OK" << std::endl;

        info.solveTime = end - start;
        info.relativeError = (x - xe).norm() / xe.norm();

        std::cerr << "Relative error: " << info.relativeError << std::endl;
    }

    return info;
}

void processFile(const boost::filesystem::path &file) {
    MatrixInfo info = processMatrix(file.string());

    std::cout << file.filename().string() << ","
              << info.rows << ","
              << info.nonZeros << ","
              << info.loadTime.count() << ","
              << info.solveTime.count() << ","
              << info.relativeError << std::endl;
}

void processDirectory(const boost::filesystem::path &directory, bool wait = false) {
    namespace fs = boost::filesystem;
    namespace algo = boost::algorithm;

    std::cerr << "Process ID: " << getpid() << std::endl;
    std::cerr << "Working Directory: " << directory << std::endl;

    std::cout << "name,rows,nonZeros,loadTime,solveTime,relativeError" << std::endl;

    for (auto &file : fs::directory_iterator(directory)) {
        const fs::path &filepath = file.path();

        std::string filename = filepath.filename().string();

        if (!algo::ends_with(filename, ".mtx.gz")) {
            std::cerr << "Ignoring file " << filename << std::endl;
            continue;
        }

        if (wait) {
            std::cerr << "Press a key to continue... ";
            std::cin.get();
        }

        processFile(filepath);
    }
}

int main(int argc, char **argv) {
    namespace fs = boost::filesystem;

    fs::path inputPath;

    if (argc == 1) {
        inputPath = ".";
    } else if (argc == 2) {
        inputPath = argv[1];
    } else {
        std::cerr << "Unexpected command line arguments!" << std::endl;
        return 1;
    }

    if (fs::is_directory(inputPath)) {
        processDirectory(inputPath);
    } else {
        processFile(inputPath);
    }

    return 0;
}
