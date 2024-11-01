import numpy as np
import matplotlib.pyplot as plt

# Define function returning solar flux [1368 W*m^-2] over time
def solarflux(t):

    return 1368

# Define function returning volcanism coefficient over time
def phi_volcano(t, year=0):
    
    # function inputs:
    #       t: time (seconds) after eruption
    #
    # function outputs:
    #       factor: (1 - factor) represents the percent reduction in incoming radiation

    yr_to_sec_factor = 365*24*60*60
    factor_0 = 0.74
    factor = 0

    factors = [factor_0, (factor+0.81), (factor+0.91), (factor+0.94), 1]
    t_yrs   = [year,    year+0.5,  year+1.5,  year+2.5,  year+6.5]
    t_secs  = [i * yr_to_sec_factor for i in t_yrs]

    interp_secs = np.interp(t, t_secs, factors)

    if (t < year * yr_to_sec_factor):
        interp_secs = 1

    return interp_secs

def solarflux(t):
    if (t <= 4570000000*365*24*60*60):
        return (1368*0.28/4.57)*t/(1000000000*365*24*60*60) + 1368*0.72
    
    else:
        return 0
    
# Define function returning temperature and zone-dependent albedo
def albedo_t(albedo_0, albedo_ice, T, ALBEDO_TEMP_DEPENDENT=True):

    # function inputs:
    #       albedo_0: zonally-average initial albedo
    #       T: temperature (Kelvin)
    #
    # function outputs:
    #       albedo: albedo based on temp

    # threshold temp below which we see albedo take value of albedo_ice
    Ti = 260
    # threshold temp below which we see albedo increasing quadratically
    T0 = 290

    if not ALBEDO_TEMP_DEPENDENT:
        return albedo_0

    if (T >= T0):
        return albedo_0
    elif (Ti < T < T0):
        return albedo_0 + (albedo_ice - albedo_0)*((T-T0)**2/(Ti-T0)**2)
    elif (T <= Ti):
        return albedo_ice

# secs = np.arange(0, 5000000000*365*24*60*60, 100000000*365*24*60*60)
# print(secs)
# e = []
# for p in secs:
#     e.append(solarflux(p))
# print(e)
# plt.plot(secs/(365*24*60*60), e)
# plt.show()