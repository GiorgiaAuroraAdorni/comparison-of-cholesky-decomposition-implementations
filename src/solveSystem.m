function [x, m] = solveSystem(A, b)
    unix('vm_stat');
    mem = memory;
    mem_in = mem.MemAvailableAllArrays;

    x = A \ b;

    mem = memory;
    mem_out = mem.MemAvailableAllArrays;
    
    m = mem_out - mem_in;
end
