clc
clear all
format short

%%
%memory
profile on -history -timer 'real' %FIXME   

fileList = getFileList('matrices');

for i = 1:numel(fileList)
    fileName = string(fileList(i));
    
    [matrixSize, relativeError] = solveSystem(fileName);
    relativeError
    matrixSize
end

p = profile('info');
s = profile('status');
% profile viewer
fun = p.FunctionTable;

numEvents = size(p.FunctionHistory,2);
% for n = 1:numEvents
%     name = fun(i).FunctionName;
%     name
%     if name == 'prova'
%         p.FunctionTable.TotalTime
%     end
%     
% %     if p.FunctionHistory(1,n) == 0
% %         disp(['Entered ' name]);
% %     else
% %         disp(['Exited ' name]);
% %     end
% end


% a = fun.TotalTime;
% a
% size = length(a);
% 
% fun.FunctionName{1, 2}
% for i = 0:size
%     if (fun.FunctionName(i) == 'prova')
%     
%     fun.TotalTime
% 
% end
% end


%memory