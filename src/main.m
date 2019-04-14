clc
clear
format short

%%
% memory  % only in Windows

fileList = getFileList('matrices');

matrixSizes = zeros(numel(fileList), 1);
realTimes = zeros(numel(fileList), 1);
relativeErrors = zeros(numel(fileList), 1);

for i = 1:numel(fileList)
    profile on -history
    
    fileName = string(fileList(i));
    
    [relativeErrors(i), matrixSizes(i)] = loadAndSolve(fileName); % %#ok<NOPTS>
    
    p = profile('info');
    % s = profile('status');
    fun = p.FunctionTable;

    for j = 1:length(fun)
        f = fun(j);

        if f.FunctionName == "solveSystem"
           realTimes(i) = f.TotalTime;  % %#ok<NOPTS>
        end
    end
end

[matrixSizesSorted, idx] = sort(matrixSizes);
realTimesSorted = realTimes(idx);

loglog(matrixSizesSorted, realTimesSorted, '-s');
