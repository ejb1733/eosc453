import numpy as np
import matplotlib.pyplot as plt
from science.ODEs import ODEs_T
from utilities.solvers import rk4 

# T0s = np.array([1,2,3,4,5,6])
T0s = np.zeros(6)
# T0s = np.array([5.080, 5.567, 5.481, 12.467, 12.151, 4.167])
# T0s = np.array([26.456,  28.244,  32.145,  51.676, 48.116, -28.183])
# T0s = np.array([250, 300, 315, 310, 295, 272])
T0s = np.array([265.467, 279.053, 281.506, 289.392, 286.452, 271.334])

x0=50000000
xf=400000000
N=5000

outps = rk4(fxy=ODEs_T, x0=x0, xf=xf, y0=T0s, N=N)

plt.plot(outps[0], outps[1])
plt.legend(['1','2','3','4','5','6'])
plt.title(f'temp over time for x0={x0}, xf={xf}, h={(xf-x0)/N}')
plt.suptitle(f'initial conds: {T0s}')
plt.show()

print(outps[1][len(outps[1])-1])