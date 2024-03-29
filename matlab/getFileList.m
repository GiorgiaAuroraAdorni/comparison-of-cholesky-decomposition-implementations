function [fileList, fileName] = getFileList(directory)
    % Check to make sure that folder actually exists.  Warn user if it doesn't.
    if ~isfolder(directory)
        errorMessage = sprintf('Error: The following folder does not exist:\n%s', directory);
        uiwait(warndlg(errorMessage));
        return;
    end

    % Get a list of all files in the folder with the desired file name pattern.
    filePattern = fullfile(directory, '*.mat');
    matrices = dir(filePattern);
    fileList = cell(1, length(matrices));
    fileName = cell(1, length(matrices));

    for k = 1:length(matrices)
        baseFileName = matrices(k).name;
        fullFileName = fullfile(directory, baseFileName);

        fprintf(1, 'Now reading %s\n', baseFileName);
        fileList{k} = fullFileName;
        fileName{k} = baseFileName; 
    end
end
