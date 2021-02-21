function [c,n] = clsq(A,dim);
    % solves the constrained least squares Problem
    % A (c n)' ~ 0 subject to norm(n,2)=1
    % length(n) = dim
    % [c,n] = clsq(A,dim)
    [m,p] = size(A)
    if p < dim+1, error ('not enough unknowns parameter'); end;
    if m < dim, error ('not enough equations'); end;
    m = min (m, p)
    triu (qr (A))
    R = triu (qr (A))
%     S = p-dim+1:m
%     e = p-dim+1:p
    S = p-dim+1
    E1 = m
    E2 = p
    R(p-dim+1:m,p-dim+1:p)
    [U,S,V] = svd(R(p-dim+1:m,p-dim+1:p))
    n = V(:,dim)
    para1 = -R(1:p-dim,1:p-dim)
    para2 = R(1:p-dim,p-dim+1:p)

    E1 = p-dim
    E2 = p-dim+1
%     c2 = inv(para1)*para2
%     c1 = para1 \ para2
    c = -R(1:p-dim,1:p-dim)\R(1:p-dim,p-dim+1:p)*n
    
    