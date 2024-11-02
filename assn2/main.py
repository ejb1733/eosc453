import numpy as np
import matplotlib.pyplot as plt
from science.ODEs import ODEs_T, eruption_year
from utilities.solvers import rk4 
from utilities.plotters import plottr
from data.constants import *

# T0s = np.zeros(6)

T0s = np.array([250, 285, 295, 300, 290, 260])

T0s = np.array([267.04120995, 283.23383646, 292.40219505, 288.59584075,
 284.80776862, 268.96382257])

x0 = 0
# xf = 3.1536*10**9 # 100 years in seconds
xf = 15 * YEARS_TO_SECONDS
xf_5byr=5000000000*365*24*60*60
delta_x = xf - x0
N=10000

delta_x_yrs = delta_x / 60 / 60 / 24 / 365

outps = rk4(fxy=ODEs_T, x0=x0, xf=xf, y0=T0s, N=N)

plot = plottr(outps[0]/YEARS_TO_SECONDS, outps[1]-273.15, 
              xlab='time (yrs)', ylab='temperature (\xb0C)',
            #   title=f'emissivity $\u03B5 = {EPSILON}$',
              title=f'Temperature Evolution of Six Zones With Volcanism',
              y0=-10, yf=25,
              xline=eruption_year)

print(outps[1][len(outps[1])-1])
print(f'years integrated over: {delta_x_yrs}')