import numpy as np
import matplotlib.pyplot as plt
from science.ODEs import ODEs_T
from utilities.solvers import rk4 
from utilities.plotters import plottr

# T0s = np.array([1,2,3,4,5,6])
# T0s = np.zeros(6)
# [255.75704983+0.j 268.60289644+0.j 284.0741405 +0.j 282.44674481+0.j
#  279.09021758+0.j 263.95332606+0.j]

# T0s = np.array([5.080, 5.567, 5.481, 12.467, 12.151, 4.167])
# T0s = np.array([26.456,  28.244,  32.145,  51.676, 48.116, -28.183])

T0s = np.array([250, 300, 315, 310, 295, 270])
# T0s = [255.81639372, 268.66487843, 284.12032535, 282.47942064, 279.12083437, 263.9811927]

# x0=50000000
x0 = 0
xf = 500000000
xf_5byr=5000000000*365*24*60*60
delta_x = xf - x0
N=10000

delta_x_yrs = delta_x / 60 / 60 / 24 / 365

outps = rk4(fxy=ODEs_T, x0=x0, xf=xf, y0=T0s, N=N)

plot = plottr(outps[0], outps[1], 
              xlab='time (s)', ylab='temprature (K)',
              title=f'temp over time for x0={x0}, xf={xf}, h={(xf-x0)/N}',
              suptitle=f'initial conds: {T0s}')

print(outps[1][len(outps[1])-1])
print(f'years integrated over: {delta_x_yrs}')