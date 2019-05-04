function [matrixSize, nonZeros, solveTime, loadTime, relativeError] = processFile(fileName, matrixName)
  profile on -history
  
  [relativeError, matrixSize, nonZeros] = loadAndSolve(fileName, matrixName);

  p = profile('info');
  fun = p.FunctionTable;

  for j = 1:length(fun)
      f = fun(j);

      if f.FunctionName == "solveSystem"
         solveTime = f.TotalTime;
      elseif f.FunctionName == "loadMatrices"
         loadTime = f.TotalTime;
      end
  end
end
