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
    # print('crop_r',crop_r)
    U,S,V = np.linalg.svd(crop_r)
    print('U',U)
    print('S',S)    
    print('V',V)    
    n = V[:,dim - 1]
    print('n',n)    
    para_1 = -r[0:p-dim,0:p - dim]
    para_3 = r[0:p-dim,p-dim:p]
    print('para_1',para_1)
    print('para_3',para_3)

    invP1 = np.linalg.inv(para_1)
    c = invP1.dot(para_3).dot(n)
    return c,n


Px = np.arange(1,11)
Py = [ 0.2,1.0,2.6,3.6,4.9,5.3,6.5,7.8,8.0,9.0]

Qx = np.array([0,1,3,5,6,7])
Qy = [12,8,6,3,3,0]
print('Px',Px)
print('Qx',Qx)
plt.plot(Px,Py,"o")
plt.plot(Qx,Qy,"x")


A_list = []
for i in range(len(Px)):
    A_list.append([1,0,Px[i],Py[i]])

for i in range(len(Qx)):
    A_list.append([0,1,Qy[i],-Qx[i]])



A = np.array(A_list)
c,n = clsq(A,2)

print('c',c)
print('n',n)
print('Px',Px)
print()
fit_py = (-c[0] - n[0] * Px )/n[1]
print('fit_py',fit_py)
# print('e',(-c[1] + n[1] * Qx ))
print('n[0]',n[0])
print('Qx',Qx)
fit_Qy = (-c[1] + n[1] * Qx )/n[0]
plt.plot(Px,fit_py)
plt.plot(Qx,fit_Qy)
plt.xlim(-4,12)
plt.ylim(0,13)
plt.show()

print('hello')