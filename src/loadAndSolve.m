function [e, n] = loadAndSolve(fileName)
    matrix = load(fileName);
    A = matrix.Problem.A;

    n = size(A, 1);
    xe = ones(n, 1);
    b = A * xe;
    
    fprintf(1, '\nNow solving %s\n', fileName);
    x = solveSystem(A, b);

    % precision or relative error
    e = norm(x - xe) / norm(xe);  
end
