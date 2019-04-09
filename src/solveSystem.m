function [n, e] = solveSystem(fileName)
    matrix = load(fileName);
    A = matrix.Problem.A;

    n = size(A, 1);
    xe = ones(n, 1);
    b = A * xe;
    x = A \ b;

    % precision or relative error
    e = norm(x - xe) / norm(xe);  
end
