import numpy as np

from .forcings import solarflux, sigma
from .data import constants as const

# Define function for returning n ODEs in accordance with our temperature model
def ODEs_T(t,T, VOLC=False):
  
    # The inputs to the function are:
    #         t (float): the current time in our box-model evolution
    #         T (1D np.arr): an array of size 6 representing each zone's temperature at time t
    #         VOLC (bool): True when considering effects of volcanism, False otherwise

    # The output of the function is:
    #         ODEs: an array of size 9 where each entry is the net flux in/out of that box

    # initialize a size 9 array which will be updated with ODEs
    n = len(T)
    ODEs = np.zeros(n)

    sigma = 1
    # if VOLC:
    #     sigma = sigma(t)

    ODEs[0] = (1/const.pcz_avgs[0]) * (const.GAMMAS[0] * (1-const.alpha_skys[0])*(1-const.alpha_avgs[0])*sigma*const.SOLAR_CONST - const.TAU*const.SIGMA_B*T[0]**4) + const.thermal_exchange_rates[0]/(const.zone_sareas[0]*const.pcz_avgs[0])*(T[1]-T[0])

    for r in range(1,n-1):
        # calculate temperature at time t for each ODE
        ODEs[r] = (1/const.pcz_avgs[r]) * (const.GAMMAS[r] * (1-const.alpha_skys[r])*(1-const.alpha_avgs[r])*sigma*const.SOLAR_CONST - const.TAU*const.SIGMA_B*T[r]**4) + 1/(const.zone_sareas[r]*const.pcz_avgs[r])*(-const.thermal_exchange_rates[r-1]*(T[r]-T[r-1]) + const.thermal_exchange_rates[r]*(T[r+1]-T[r]))

    ODEs[5] = (1/const.pcz_avgs[5]) * (const.GAMMAS[5] * (1-const.alpha_skys[5])*(1-const.alpha_avgs[5])*sigma*const.SOLAR_CONST - const.TAU*const.SIGMA_B*T[5]**4) + const.thermal_exchange_rates[4]/(const.zone_sareas[5]*const.pcz_avgs[5])*(T[5]-T[4])

    return ODEs

out = ODEs_T(0,np.zeros(6))
print(f'T=0s:   {out}')