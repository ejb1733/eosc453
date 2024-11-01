import numpy as np
import matplotlib.pyplot as plt
from science.ODEs import ODEs_T
from utilities.solvers import rk4 
from utilities.plotters import plottr

# T0s = np.zeros(6)

T0s = np.array([250, 285, 295, 300, 290, 260])

x0 = 0
xf = 3.1536*10**9
xf_5byr=5000000000*365*24*60*60
delta_x = xf - x0
N=10000

delta_x_yrs = delta_x / 60 / 60 / 24 / 365

outps = rk4(fxy=ODEs_T, x0=x0, xf=xf, y0=T0s, N=N)

plot = plottr(outps[0], outps[1], 
              xlab='time (s)', ylab='temprature (K)',
              title=f'temp over time for x0={x0}, xf={xf}, h={(xf-x0)/N}',
              suptitle=f'Temperature vs Time')

print(outps[1][len(outps[1])-1])
print(f'years integrated over: {delta_x_yrs}')