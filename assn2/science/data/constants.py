import numpy as np

TAU = 0.63
RADIUS_E = 6371 * 10**3
SIGMA_B = 5.6696 * 10**-8
SOLAR_CONST = 1368
SAREA_EARTH = 4*np.pi*RADIUS_E**2

GAMMAS = np.array([0.1076, 0.2277, 0.3045, 0.3045, 0.2277, 0.1076])

# surface fraction
# estimates for zones 1-6: [  z1  ,   z2  ,   z3  ,   z4  ,   z5  ,   z6  ]  
AREA_FRACTIONS = np.array( [0.0670, 0.1830, 0.2500, 0.2500, 0.1830, 0.0670])
LAND_FRACTIONS = np.array( [0     , 0.7   , 0.20  , 0.32  , 0.50  ,  0.35 ])
OCEAN_FRACTIONS = np.array([0.52  , 0.93  , 0.80  , 0.68  , 0.50  ,  0.50 ])
ICE_FRACTIONS = np.array(  [0.48  , 0     , 0.80  , 0     , 0     ,  0.15 ])

pcz_avgs = np.empty(shape=6); pcz_avgs.fill(50000000)

alpha_skys = np.empty(shape=6); alpha_skys.fill(0.7)

alpha_avgs = np.empty(shape=6); alpha_avgs.fill(0.5)

zone_sareas = np.empty(shape=6)
for a in range(6):
    zone_sareas[a] = AREA_FRACTIONS[a] * SAREA_EARTH

# intra-zonal constants
boundary_lengths = np.array([2.0015*10**7, 3.4667*10**7, 4.0030*10**7, 3.4667*10**7, 2.0015*10**7])
thermal_exchange_coefficients = np.array([1*10**7, 1*10**7, 1*10**7, 5*10**7, 1*10**7])
thermal_exchange_rates = boundary_lengths * thermal_exchange_coefficients

thermal_exchange_rates = np.zeros(6)

print(f'thermal exchange rates:   {thermal_exchange_rates}')

print(f'surface area of Earth: {SAREA_EARTH}')
print(f'surface area of zone 1: {zone_sareas[0]}')
print(f'fraction of earth surface area in zone 1: {zone_sareas[0]/SAREA_EARTH}')
print(f'')
print(f'')