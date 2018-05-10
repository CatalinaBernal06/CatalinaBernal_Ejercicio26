import numpy as np
import matplotlib.pyplot as plt

p = 10000000
v0 = np.random.uniform(35, 45, p)
th0 = np.random.uniform(0, (np.pi/2.0), p)
g = 9.8
datos = [[56, 66], [109, 119], [26, 36], [172, 182]]

plt.figure()
obs = 0
for dato in datos:
    d = ((v0**2)*np.sin(2*th0))/g
    cond = (d<dato[1]) & (d>dato[0])
    v0 = v0[cond]
    v0 = np.random.choice(v0, p)
    plt.hist(v0, normed = True, label = "dato " + str(obs))
    obs += 1

plt.xlabel('angulo')
plt.ylabel('probabilidad')
plt.title('Tiro parabolico')
plt.legend()
plt.savefig('angulos.pdf')
            








