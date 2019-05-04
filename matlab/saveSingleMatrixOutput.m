function saveSingleMatrixOutput(matrixName, matrixSize, nonZeros, loadTime, solveTime, relativeError)
    output = [matrixName, num2cell(matrixSize), num2cell(nonZeros), num2cell(loadTime), num2cell(solveTime), num2cell(relativeError)];
    
    filename = ['output/', matrixName, '.csv'];
    writecell(output, filename);
end
