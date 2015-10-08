import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import ode
from mpl_toolkits.mplot3d import Axes3D

sigma = 10
beta = 8/3.
rho = 28
w_0 = [10, 10, 10]
t_0 = 0

#creamos funcion adhoc para la usar el ode de scipy
def EDO(t, w, s=sigma, r=rho, b=beta):
    x, y, z = w
    return [s*(y-x), x*(r-z)-y, x*y-b*z]

#seteamos el la funcion ode para resolver el sistema de EDOS
r = ode(EDO)
r.set_integrator('dopri5') #comando para usar RK4
r.set_initial_value(w_0, t_0)

t = np.linspace(t_0, 100, 10000)

x = np.zeros(len(t))
y = np.zeros(len(t))
z = np.zeros(len(t))

#iteramos usando la funcion ode antes mencionada
for i in range(len(t)):
    r.integrate(t[i])
    x[i], y[i], z[i] = r.y


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(x, y, z)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.title("Atractor de Lorenz")
plt.show()
