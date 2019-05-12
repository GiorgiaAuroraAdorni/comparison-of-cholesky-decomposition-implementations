#include "utils/MatrixMarket.h"

#include <Eigen/Eigen>

#if ENABLE_MKL
#include <Eigen/PardisoSupport>
#endif

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
Eigen::VectorXd solveSystem(const SparseMatrixType &A, const Eigen::VectorXd &b) {
    using namespace Eigen;

#if ENABLE_MKL
    PardisoLDLT<SparseMatrixType> solver(A);
#else
    SimplicialLDLT<SparseMatrixType> solver(A);
#endif

    return solver.solve(b);
}

template<typename SparseMatrixType>
MatrixInfo processMatrix(const std::string &filename) {
    using namespace Eigen;

    MatrixInfo info {};
    SparseMatrixType A;

    {
        std::cerr << "Loading matrix '" << filename << "'... " << std::flush;

        auto start = std::chrono::high_resolution_clock::now();

        SparseMatrixType matrix;
        bool result = loadMarketGzip(matrix, filename);

        A = matrix.template selfadjointView<Lower>();

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

template<typename SparseMatrixType>
void processFile(const boost::filesystem::path &file) {
    MatrixInfo info = processMatrix<SparseMatrixType>(file.string());

    std::cout << file.filename().string() << ","
              << info.rows << ","
              << info.nonZeros << ","
              << info.loadTime.count() << ","
              << info.solveTime.count() << ","
              << info.relativeError << std::endl;
}

template<typename SparseMatrixType>
void processDirectory(const boost::filesystem::path &directory, bool wait = false) {
    namespace fs = boost::filesystem;
    namespace algo = boost::algorithm;

    //std::cerr << "Process ID: " << getpid() << std::endl;
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

        processFile<SparseMatrixType>(filepath);
    }
}

template<typename SparseMatrixType>
void processInput(const boost::filesystem::path &inputPath) {
    namespace fs = boost::filesystem;

    if (fs::is_directory(inputPath)) {
        processDirectory<SparseMatrixType>(inputPath);
    } else {
        processFile<SparseMatrixType>(inputPath);
    }
}

int main(int argc, char **argv) {
    namespace fs = boost::filesystem;

    fs::path inputPath;
    std::string indexSize;

    if (argc == 1) {
        inputPath = ".";
        indexSize = "64";
    } else if (argc == 2) {
        inputPath = argv[1];
        indexSize = "64";
    } else if (argc == 3) {
        inputPath = argv[1];
        indexSize = argv[2];
    } else {
        std::cerr << "Unexpected command line arguments!" << std::endl;
        return 1;
    }

    using namespace Eigen;

#if ENABLE_MKL
    std::cerr << "Sparse Cholesky implementation: MKL" << std::endl;
#else
    std::cerr << "Sparse Cholesky implementation: Eigen" << std::endl;
#endif

    if (indexSize == "32") {
#if ENABLE_MKL
        std::cerr << "MKL requires 64-bit sparse matrix indices" << std::endl;
#else
        typedef SparseMatrix<double, ColMajor, int32_t> SM;
        std::cerr << "Sparse matrix index size: " << indexSize << " bit" << std::endl;

        processInput<SM>(inputPath);
#endif
    } else if (indexSize == "64") {
        typedef SparseMatrix<double, ColMajor, int64_t> SM;
        std::cerr << "Sparse matrix index size: " << indexSize << " bit" << std::endl;

        processInput<SM>(inputPath);
    } else {
        std::cerr << "Unexpected value for sparse matrix index size: " << indexSize << std::endl;
    }

    return 0;
}
