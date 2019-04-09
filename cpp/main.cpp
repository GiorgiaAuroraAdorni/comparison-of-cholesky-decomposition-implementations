#include "utils/MarketIO.h"

#include <Eigen/Sparse>
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

    SparseMatrix<double> mat;
    SparseMatrix<double> mat2;

    std::cout << "Loading matrices... " << std::flush;

    bool result;

    result = loadMarket(mat, "cfd1.mtx");
    result &= loadMarketGzip(mat2, "cfd1.mtx.gz");

    std::cout << (result ? "OK" : "ERROR") << std::endl;

    std::cout << mat.rows() << "x" << mat.cols() << " " << mat.nonZeros() << std::endl;
    std::cout << mat2.rows() << "x" << mat2.cols() << " " << mat2.nonZeros() << std::endl;

    return 0;
}
