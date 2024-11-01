import numpy as np

from .forcings import solarflux, phi_volcano, albedo_t
from data.constants import *

okwtf = 1

# Define function for returning n ODEs in accordance with our temperature model
def ODEs_T(t,T, VOLC=True, ALBEDO_TEMP_DEPENDENT=True):
  
    # The inputs to the function are:
    #         t (float): the current time in our box-model evolution
    #         T (1D np.arr): an array of size 6 representing each zone's temperature at time t
    #         VOLC (bool): True when considering effects of volcanism, False otherwise
    #         ALBEDO_TEMP_DEPENDENT (bool): True when considering albedo as dependent on temperature

    # The output of the function is:
    #         ODEs: an array of size 6 where each entry is the temperature of our zone

    # initialize a size 6 array which will be updated with ODEs
    n = len(T)
    ODEs = np.zeros(n)

    phi = 1
    if VOLC:
        phi = phi_volcano(t,year=60)

    # print(f'GAMMAS: {GAMMAS}, ALBEDOS AVGS: {albedo_avgs}')

    ODEs[0] = (1/PCZ_AVGS[0]) * (GAMMAS[0] * (1-ALBEDO_SKYS[0])*(1-albedo_t(ALBEDO_AVGS[0],ALBEDO_ICE,abs(T[0]),ALBEDO_TEMP_DEPENDENT))*phi*SOLAR_CONST - EPSILON*TAU*SIGMA_B*T[0]**4) + thermal_exchange_rates[0]/(ZONE_SAREAS[0]*PCZ_AVGS[0])*(T[1]-T[0])

    for r in range(1,n-1):
        # calculate temperature at time t for each ODE
        ODEs[r] = (1/PCZ_AVGS[r]) * (GAMMAS[r] * (1-ALBEDO_SKYS[r])*(1-albedo_t(ALBEDO_AVGS[r],ALBEDO_ICE,abs(T[r]),ALBEDO_TEMP_DEPENDENT))*phi*SOLAR_CONST - EPSILON*TAU*SIGMA_B*T[r]**4) + 1/(ZONE_SAREAS[r]*PCZ_AVGS[r])*(-thermal_exchange_rates[r-1]*(T[r]-T[r-1]) + thermal_exchange_rates[r]*(T[r+1]-T[r]))

    ODEs[5] = (1/PCZ_AVGS[5]) * (GAMMAS[5] * (1-ALBEDO_SKYS[5])*(1-albedo_t(ALBEDO_AVGS[5],ALBEDO_ICE,abs(T[5]),ALBEDO_TEMP_DEPENDENT))*phi*SOLAR_CONST - EPSILON*TAU*SIGMA_B*T[5]**4) - thermal_exchange_rates[4]/(ZONE_SAREAS[5]*PCZ_AVGS[5])*(T[5]-T[4])

    return ODEs

out = ODEs_T(0,np.zeros(6))
print(f'T=0s:   {out}')