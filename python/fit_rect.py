import matplotlib.pyplot as plt #繪圖用的模組
from mpl_toolkits.mplot3d import Axes3D #繪製3D座標的函式
import numpy as np

def clsq(A,dim):
    # print(A.shape)
    m , p = A.shape
    m=min(m,p)
    # print('m',m)
    # print('p',p)
    # print('A',A)
    q, r = np.linalg.qr(A,mode='complete')
    # print('q',q)
    # print('r',r)


    # print(r[p-dim:m,p-dim:p])
    crop_r = r[p-dim:m,p-dim:p]
    U,S,V = np.linalg.svd(crop_r)
    # print('U',U)
    # print('S',S)    
    # print('V',V)    
    n = V[:,dim - 1]
    # print('n',n)    
    para_1 = -r[0:p-dim,0:p - dim]
    para_3 = r[0:p-dim,p-dim:p]
    print('para_1',para_1)
    print('para_3',para_3)
    c =(para_3 / para_1).dot(n)
    return c,n


Px = np.arange(1,11)

Py = [ 0.2,1.0,2.6,3.6,4.9,5.3,6.5,7.8,8.0,9.0]
plt.plot(Px,Py,"o")
A_list = []
for i in range(len(Px)):
    # A = np.array([[np.ones(Px.size)],[Px],[Py]])
    A_list.append([1,Px[i],Py[i]])
A = np.array(A_list)
c,n = clsq(A,2)

print('c',c)
print('n',n)
fit_py = (-c[0] - n[0] * Px )/n[1]
print('fit_py',fit_py)


plt.plot(Px,fit_py)
plt.show()

print('hello')