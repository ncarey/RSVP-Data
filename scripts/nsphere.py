import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d

N = 600
dim = 4

norm = np.random.normal
normal_deviates = norm(size=(dim, N))

radius = np.sqrt((normal_deviates**2).sum(axis=0))
points = normal_deviates/radius

unif = np.random.uniform
uniform_deviates = unif(0,1,size=(1, N))
radius2 = uniform_deviates**(1.0/dim)

points = points * radius2

points = points * 4

fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
ax.scatter(*points)
ax.set_aspect('equal')
plt.show()
