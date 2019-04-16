#include "utils/MatrixMarket.h"

#include <Eigen/Eigen>

#include <iostream>

int main() {
    using namespace Eigen;

    std::string filename = "ex15.mtx.gz";
    SparseMatrix<double> matrix;

    std::cout << "Loading matrix '" << filename << "'... " << std::flush;

    bool result = loadMarketGzip(matrix, filename);
    auto A = matrix.selfadjointView<Lower>();

    std::cout << (result ? "OK" : "ERROR") << std::endl;
    std::cout << A.rows() << "x" << A.cols() << std::endl;

    VectorXd xe = VectorXd::Ones(A.rows());
    VectorXd b = A * xe;

    SimplicialLDLT<SparseMatrix<double>> solver(A);

    VectorXd x = solver.solve(b);

    double relativeError = (x - xe).norm() / xe.norm();

    std::cout << x << std::endl;
    std::cout << "Relative error: " << relativeError << std::endl;

    return 0;
}
