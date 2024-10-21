import numpy as np
import matplotlib.pyplot as plt

# Define function returning solar flux [1368 W*m^-2] over time
def solarflux(t):

    return 1368

# Define function returning volcanism coefficient over time
def sigma(t, VOLC=False):
    
    # function inputs:
    #       t: time (seconds) after eruption
    #
    # function outputs:
    #       factor: (1 - factor) represents the percent reduction in incoming radiation

    factors = [0.74, 0.81, 0.91, 0.94, 1]
    t_yrs   = [0,    0.5,  1.5,  2.5,  6.5]
    t_secs  = [i * 365*24*60*60 for i in t_yrs]

    interp_secs = np.interp(t, t_secs, factors)

    return interp_secs

# print('yrs'), print(sigma(1*365*24*3600))
# print('secs'), sigma(365*60*24*60)

# yr_to_secs_factor = 365*24*60*60

# secs = np.arange(0,3.5*yr_to_secs_factor, 10000)
# e = sigma(secs)
# print(e)
# plt.plot(secs/yr_to_secs_factor,e)
# plt.show()