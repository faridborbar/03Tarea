import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import ode
from mpl_toolkits.mplot3d import Axes3D


sigma = 10
beta = 8/3.
rho = 28
w0 = [5, 5, 5]
t0 = 0

#creamos funcion adhoc para la usar el ode de scipy
def Lorentz(t, w, s=sigma, r=rho, b=beta):
    X, Y, Z = w
    return [s*(Y-X), X*(r-Z)-Y, X*Y-b*Z]

#seteamos el la funcion ode para resolver el sistema de EDOS
r = ode(Lorentz)
r.set_integrator('dopri5') #comando para usar RK4
r.set_initial_value(w0, t0)

t = np.linspace(t0, 50, 10000)

X = np.zeros(len(t))
Y = np.zeros(len(t))
Z = np.zeros(len(t))

#iteramos usando la funcion ode antes mencionada
for i in range(len(t)):
    r.integrate(t[i])
    X[i], Y[i], Z[i] = r.y


fig = plt.figure()
figura = fig.add_subplot(111, projection='3d')

figura.plot(X, Y, Z)

figura.set_xlabel('variable x')
figura.set_ylabel('variable y')
figura.set_zlabel('variable z')
plt.title("Atractor de Lorenz")
plt.show()