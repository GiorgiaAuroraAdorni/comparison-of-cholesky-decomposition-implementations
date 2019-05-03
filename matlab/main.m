clc
clear
format short
profile off

%%

[fileList, matrixList] = getFileList('matrices');

matrixSizes = zeros(numel(fileList), 1);
nonZeros = zeros(numel(fileList), 1);
loadTimes = zeros(numel(fileList), 1);
solveTimes = zeros(numel(fileList), 1);
relativeErrors = zeros(numel(fileList), 1);

for i = 1:numel(fileList)
    input('Press a key to continue...');

    profile on -history
    
    fileName = string(fileList(i));
    matrixName = string(matrixList(i));
    
    [relativeErrors(i), matrixSizes(i), nonZeros(i)] = loadAndSolve(fileName, matrixName); % %#ok<NOPTS>
    
    p = profile('info');
    fun = p.FunctionTable;

    for j = 1:length(fun)
        f = fun(j);

        if f.FunctionName == "solveSystem"
           solveTimes(i) = f.TotalTime;
        elseif f.FunctionName == "loadMatrices"
           loadTimes(i) = f.TotalTime;
        end
    end
end

saveOutput(matrixList, matrixSizes, nonZeros, loadTimes, solveTimes, relativeErrors)


[matrixSizesSorted, idx] = sort(matrixSizes);

figure(1)

subplot(1,3,1, 'XScale', 'log', 'YScale', 'log');
realTimesSorted = solveTimes(idx);
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

% subplot(1,3,3, 'XScale', 'log', 'YScale', 'log');
% memoriesSorted = memories(idx);
% loglog(matrixSizesSorted, memoriesSorted, '-s');
% title('Plot of the memory needed to solve the systems')
% xlabel('Matrix size') 
% ylabel('Memory')
