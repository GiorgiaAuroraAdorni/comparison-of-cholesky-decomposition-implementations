//
// Created by Elia Cereda on 2019-04-16.
//

#ifndef MATRIXMARKET_H
#define MATRIXMARKET_H

#include "../third-party/MarketIO.h"

#include <boost/iostreams/filtering_stream.hpp>
#include <boost/iostreams/filter/gzip.hpp>

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

#endif //MATRIXMARKET_H
