#include "utils/MarketIO.h"

#include <Eigen/Eigen>
#include <boost/iostreams/filtering_stream.hpp>
#include <boost/iostreams/filter/gzip.hpp>

#include <iostream>
#include <fstream>

template<typename SparseMatrixType>
bool loadMarketGzip(SparseMatrixType& mat, const std::string& filename) {
    namespace io = boost::iostreams;

    std::ifstream file(filename, std::ios::in | std::ios::binary);
    io::filtering_istream input;
    input.push(io::gzip_decompressor());
    input.push(file);

    bool result = Eigen::loadMarket(mat, input);

    file.close();

    return result;
}

int main() {
    using namespace Eigen;

    SparseMatrix<double> A;

    std::cout << "Loading matrix... " << std::flush;

    bool result = loadMarketGzip(A, "ex15.mtx.gz");

    std::cout << (result ? "OK" : "ERROR") << std::endl;
    std::cout << A.rows() << "x" << A.cols() << ", " << A.nonZeros() << " non-zeroes" << std::endl;

    VectorXd xe = VectorXd::Ones(A.rows());
    VectorXd b = A * xe;

    SparseLU<SparseMatrix<double>> lu(A);

    VectorXd x = lu.solve(b);

    double relativeError = (x - xe).norm() / xe.norm();

    std::cout << x << std::endl;
    std::cout << "Relative error: " << relativeError << std::endl;

    return 0;
}
