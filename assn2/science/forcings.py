import numpy as np
import matplotlib.pyplot as plt

# Define function returning volcanism coefficient over time
def phi_volcano(t, year=0):
    
    # function inputs:
    #       t: time (seconds) after eruption
    #
    # function outputs:
    #       interp_secs: (1 - interp_secs) represents the reduction in incoming radiation

    yr_to_sec_factor = 365*24*60*60


    factor_0 = 0.74
    factor_2 = 0.48

    # first 'factors' is Pinatubo direct radiation data from Figure 2  in Robock (2000)
    # second 'factors' is "doubling" Pinatubo direct radiation data
    factors = [factor_0, (0.81), (0.91), (0.94), 1]
    # factors = [factor_2, (0.55), (0.75), (0.90), 1]

    # first 't_yrs' is pinatubo's residence timescale,
    # second 't_yrs' is double pinatubo's residence timescale
    t_yrs   = [year,    year+0.5,  year+1.5,  year+2.5,  year+6.5]
    # t_yrs   = [year,    year + 1,  year + 3,  year + 5,  year + 13]

    t_secs  = [i * yr_to_sec_factor for i in t_yrs]

    interp_secs = np.interp(t, t_secs, factors)

    if (t < year * yr_to_sec_factor):
        interp_secs = 1

    return interp_secs
    
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