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

figure(1)
subplot(1,3,1, 'XScale', 'log', 'YScale', 'log');
[matrixSizesSorted, idx] = sort(matrixSizes);
realTimesSorted = realTimes(idx);

loglog(matrixSizesSorted, realTimesSorted, '-s');
title('Plot of the time required to calculate the solution of the systems')
xlabel('Matrix size') 
ylabel('Time (seconds)') 

subplot(1,3,2, 'XScale', 'log', 'YScale', 'log');
relativeErrorsSorted = relativeErrors(idx);

loglog(matrixSizesSorted, relativeErrorsSorted, '-s');

title('Plot of the relative errors of the systems')
xlabel('Matrix size') 
ylabel('Relative Error') 

subplot(1,3,3, 'XScale', 'log', 'YScale', 'log');
title('Plot of the memory needed to solve the systems')
xlabel('Matrix size') 
ylabel('Memory') 
