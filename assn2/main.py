import numpy as np
import matplotlib.pyplot as plt
from science.ODEs import ODEs_T, eruption_year
from utilities.solvers import rk4 
from utilities.plotters import plottr
from data.constants import *

# initial temperatures for eps = 0.95 and temp-dependent albedo disabled
T0s = np.array([267.04120995, 283.23383646, 292.40219505, 288.59584075,
 284.80776862, 268.96382257])

# set initial and final time values
x0 = 0
xf = 3.1536*10**9 # 100 years in seconds
xf = 60 * YEARS_TO_SECONDS

N=10000

# run rk4
outps = rk4(fxy=ODEs_T, x0=x0, xf=xf, y0=T0s, N=N)

# plot results
plot = plottr(outps[0]/YEARS_TO_SECONDS, outps[1]-273.15, 
              xlab='time (yrs)', ylab='temperature (\xb0C)',
            #   title=f'(emissivity $\u03B5 = {EPSILON}$)',
              title=f'Temperature Evolution (2a)',
              y0=-20, yf=25,
              xline=eruption_year)

print(f'years integrated over: {xf}')