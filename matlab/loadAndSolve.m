function [e, n, nzero] = loadAndSolve(fileName, matrixName)
    matrix = loadMatrices(fileName);
    
    A = matrix.Problem.A;
    
    % returns the number of nonzero elements in A
    nzero = nnz(A); 
    
    n = size(A, 1);
    xe = ones(n, 1);
    b = A * xe;
    
    fprintf(1, '\nNow solving %s\n', matrixName);
    
    x = solveSystem(A, b);

    % precision or relative error
    e = norm(x - xe) / norm(xe);  
end
