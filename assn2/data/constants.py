import numpy as np

# define Stefan-Boltzmann constant [W * m^{-2} * K^{-4}]
SIGMA_B = 5.6696 * 10**-8

# define solar constant [W * m^{-2}]
SOLAR_CONST = 1368

# define radius of Earth [m]
RADIUS_E = 6371 * 10**3

# define surface area of Earth [m^2]
SAREA_EARTH = 4*np.pi*RADIUS_E**2

# define total emissivity of Earth
EPSILON = 1

# define atmospheric transmissivity
TAU = 0.63

# define albedos for land, water, ice
ALBEDO_SKY   = 0.2
ALBEDO_LAND  = 0.4
ALBEDO_WATER = 0.1
ALBEDO_ICE   = 0.6

# define densities [kg*m^{-3}] for land, water, ice
DENSITY_LAND  = 2500
DENSITY_WATER = 1028
DENSITY_ICE   = 900

# define thermal scale depth [m] for land, water, ice
Z_LAND  = 1
Z_WATER = 70
Z_ICE   = 1

# define specific heat capacities [J * kg * K^{-1}] for land, water, ice
C_LAND  = 790
C_WATER = 4187
C_ICE   = 2060

# define surface fraction
# estimates for zones 1-6: [  z1  ,   z2  ,   z3  ,   z4  ,   z5  ,   z6  ]  
AREA_FRACTIONS = np.array( [0.0670, 0.1830, 0.2500, 0.2500, 0.1830, 0.0670])

LAND_FRACTIONS = np.array( [0     , 0.7   , 0.20  , 0.32  , 0.50  ,  0.35 ])
WATER_FRACTIONS = np.array([0.52  , 0.93  , 0.80  , 0.68  , 0.50  ,  0.50 ])
ICE_FRACTIONS = np.array(  [0.48  , 0     , 0.80  , 0     , 0     ,  0.15 ])

# define geometric factors
# for zones 1-6:  [  z1  ,   z2  ,   z3  ,   z4  ,   z5  ,   z6  ]
GAMMAS = np.array([0.1076, 0.2277, 0.3045, 0.3045, 0.2277, 0.1076])

# define area-averaged properties
pcz_avgs = (LAND_FRACTIONS  * DENSITY_LAND  * C_LAND  * Z_LAND) + (WATER_FRACTIONS * DENSITY_WATER * C_WATER * Z_WATER) + (ICE_FRACTIONS   * DENSITY_ICE   * C_ICE   * Z_ICE)

albedo_avgs = LAND_FRACTIONS * ALBEDO_LAND + WATER_FRACTIONS * ALBEDO_WATER + ICE_FRACTIONS * ALBEDO_ICE

albedo_skys = np.empty(shape=6); albedo_skys.fill(ALBEDO_SKY)

zone_sareas = AREA_FRACTIONS * SAREA_EARTH

# intra-zonal constants
boundary_lengths = np.array([2.0015*10**7, 3.4667*10**7, 4.0030*10**7, 3.4667*10**7, 2.0015*10**7])
thermal_exchange_coefficients = np.array([1*10**7, 1*10**7, 1*10**7, 5*10**7, 1*10**7])
thermal_exchange_rates = boundary_lengths * thermal_exchange_coefficients

# start q2 by assuming all intra-zonal transfer is suppressed (k_{ij} = 0)
# thermal_exchange_rates = np.zeros(6)
# thermal_exchange_rates[2] = 2*10**14

print(f'thermal exchange rates:   {thermal_exchange_rates}')

print(f'surface area of Earth: {SAREA_EARTH}')
print(f'surface area of zone 1: {zone_sareas[0]}')
print(f'fraction of earth surface area in zone 1: {zone_sareas[0]/SAREA_EARTH}')
print(f'')
print(f'')

print(pcz_avgs)
print(albedo_avgs)
print(zone_sareas)