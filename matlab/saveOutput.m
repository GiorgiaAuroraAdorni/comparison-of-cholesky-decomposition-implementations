function saveOutput(matrixNames, matrixSizes, nonZeros, loadTimes, solveTimes, relativeErrors)
    header = ['name', 'rows', 'nonZeros', "loadTime", 'solveTime', 'relativeError'];
    header = cellstr(header);

    output = [header; matrixNames(:), num2cell(matrixSizes(:)), num2cell(nonZeros(:)), num2cell(loadTimes(:)), num2cell(solveTimes(:)), num2cell(relativeErrors(:))];

    writecell(output, 'matlabOutput.csv');
end
