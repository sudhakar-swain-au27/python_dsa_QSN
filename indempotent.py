def fun(mat):
    n = len(mat)
    res = [[0 for _ in range(n)] for _ in range(n)]
    
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j]+= (mat[i][k]*mat[k][j])
                
    print(res)
    return res==mat
    
    
    
    
mat = [[2, -2 , -4], [-1,3,4],[1,-2,-3]]
if fun(mat):
    print("Matrix is idempotent")
else:
    print("Matrix is not idempotent")