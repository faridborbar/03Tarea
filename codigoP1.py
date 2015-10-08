import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize as opti




def funcionvectorial(sn,yn,zn):
    u=0.4
    f_1=zn
    f_2=-yn-u*(yn**2 - 1)*zn

    return [f_1,f_2]

def calculoK1(sn,yn,zn):
    h=0.01
    k1_1=h * (funcionvectorial(sn,yn,zn))[0]
    k1_2=h * (funcionvectorial(sn,yn,zn))[1]
    return [k1_1,k1_2]
def calculoK2(sn,yn,zn):
    h=0.01
    k1_1=calculoK1(sn,yn,zn)[0]
    k1_2=calculoK1(sn,yn,zn)[1]
    k2_1=h * (funcionvectorial(sn + h/2.,yn + k1_1/2.,zn + k1_2/2.))[0]
    k2_2=h * (funcionvectorial(sn + h/2.,yn + k1_1/2.,zn + k1_2/2.))[1]
    return [k2_1,k2_2]

def calculoK3(sn,yn,zn):
    h=0.01
    k1_1=calculoK1(sn,yn,zn)[0]
    k1_2=calculoK1(sn,yn,zn)[1]
    k2_1=calculoK2(sn,yn,zn)[0]
    k2_2=calculoK2(sn,yn,zn)[1]
    k3_1=h * (funcionvectorial(sn +h,yn - k1_1 - 2*k2_1,zn - k1_2 - 2*k2_2))[0]
    k3_2=h * (funcionvectorial(sn +h,yn - k1_1 - 2*k2_1,zn - k1_2 - 2*k2_2))[1]
    return [k3_1,k3_2]

def Vectorsiguiente(sn,yn,zn):
    h=0.01
    sn_1 = sn + h
    yn_1 = yn + 1/6.*(calculoK1(sn,yn,zn)[0] + 4 * calculoK2(sn,yn,zn)[0] + calculoK2(sn,yn,zn)[0])
    zn_1 = zn + 1/6.*(calculoK1(sn,yn,zn)[1] + 4 * calculoK2(sn,yn,zn)[1] + calculoK2(sn,yn,zn)[1])
    return [sn_1,yn_1,zn_1]




h=0.01
N=np.arange(0,20*np.pi,h)
n=len(N)
F=[]
W_ini=[]
Y=[]
Z=[]
S=[]
W_ini=np.append(W_ini,0)
W_ini=np.append(W_ini,4)
W_ini=np.append(W_ini,0)


for i in range(0,n-1):
    h=N[i]
    a=Vectorsiguiente(W_ini[0],W_ini[1],W_ini[2])
    Y=np.append(Y,a[1])
    Z=np.append(Z,a[2])
    S=np.append(S,h)
    W_ini[0]=a[0]
    W_ini[1]=a[1]
    W_ini[2]=a[2]



plt.plot(Y,Z)
#plt.plot(S,Y)
plt.xlabel('Tiempo s')
plt.ylabel('variable y')
plt.title("Osilador Van der Pool")
plt.draw()
plt.show()
