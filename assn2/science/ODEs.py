import numpy as np

from .forcings import solarflux, sigma
# from data import constants as const
from data.constants import *

okwtf = 1

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

    # print(f'GAMMAS: {GAMMAS}, ALBEDOS AVGS: {albedo_avgs}')

    ODEs[0] = (1/pcz_avgs[0]) * (GAMMAS[0] * (1-albedo_skys[0])*(1-albedo_avgs[0])*sigma*SOLAR_CONST - TAU*SIGMA_B*T[0]**4) + thermal_exchange_rates[0]/(zone_sareas[0]*pcz_avgs[0])*(T[1]-T[0])

    for r in range(1,n-1):
        # calculate temperature at time t for each ODE
        ODEs[r] = (1/pcz_avgs[r]) * (GAMMAS[r] * (1-albedo_skys[r])*(1-albedo_avgs[r])*sigma*SOLAR_CONST - TAU*SIGMA_B*T[r]**4) + 1/(zone_sareas[r]*pcz_avgs[r])*(-thermal_exchange_rates[r-1]*(T[r]-T[r-1]) + thermal_exchange_rates[r]*(T[r+1]-T[r]))

    ODEs[5] = (1/pcz_avgs[5]) * (GAMMAS[5] * (1-albedo_skys[5])*(1-albedo_avgs[5])*sigma*SOLAR_CONST - TAU*SIGMA_B*T[5]**4) + thermal_exchange_rates[4]/(zone_sareas[5]*pcz_avgs[5])*(T[5]-T[4])

    return ODEs

out = ODEs_T(0,np.zeros(6))
print(f'T=0s:   {out}')