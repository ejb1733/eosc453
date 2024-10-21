import numpy as np
import matplotlib.pyplot as plt
from science.ODEs import ODEs_T
from science.utilities.solvers import rk4 

T0s = np.array([1,2,3,4,5,6])

outps = rk4(fxy=ODEs_T, x0=0, xf=100000, y0=T0s, N=5000)

plt.plot(outps[0], outps[1])
plt.legend(['1','2','3','4','5','6'])
plt.show()

print(outps[1][5])