function saveOutput(fileList, matrixSizes, nonZeros, loadTimes, solveTimes, relativeErrors)
	
	output = ["name",      "rows",                   "nonZeros",            "loadTime",             "solveTime",             "relativeError"; 
			  fileList(:), num2cell(matrixSizes(:)), num2cell(nonZeros(:)), num2cell(loadTimes(:)), num2cell(solveTimes(:)), num2cell(relativeErrors(:))];
   
   	writematrix(output, 'matlabOutput.csv');
end
