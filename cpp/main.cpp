#include "utils/MatrixMarket.h"

#include <Eigen/Eigen>

#include <boost/filesystem.hpp>

#include <iostream>

template<typename SparseMatrixType>
Eigen::VectorXd solveSystem(SparseMatrixType A, Eigen::VectorXd b) {
    using namespace Eigen;

    SimplicialLDLT<SparseMatrix<double>> solver(A);

    return solver.solve(b);
}

void processMatrix(std::string filename) {
    using namespace Eigen;

    SparseMatrix<double> matrix;

    std::cerr << "Processing matrix '" << filename << "'... " << std::flush;

    bool result = loadMarketGzip(matrix, filename);
    auto A = matrix.selfadjointView<Lower>();

    std::cerr << (result ? "OK" : "ERROR") << std::endl;
    std::cerr << A.rows() << "x" << A.cols() << std::endl;

    VectorXd xe = VectorXd::Ones(A.rows());
    VectorXd b = A * xe;

    VectorXd x = solveSystem(A, b);

    double relativeError = (x - xe).norm() / xe.norm();

    std::cerr << "Relative error: " << relativeError << std::endl;
}

int main(int argc, char **argv) {
    using namespace Eigen;
    namespace fs = boost::filesystem;

    std::string directory = "prova";

    for (auto &file : fs::directory_iterator(directory)) {
        processMatrix(file.path().string());
    }

    return 0;
}
