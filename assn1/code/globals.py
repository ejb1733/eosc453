import numpy as np

n_boxes = 9

# Initial carbon masses in boxes (in Gt)
M1 = 725  # Atmosphere
M2 = 725  # Surface Ocean
M3 = 0
M4 = 0
M5 = 110  # Short-lived biota
M6 = 0
M7 = 60   # Deep Ocean
M8 = 0
M9 = 0

# 1 x n array of initial masses (burdens)
mi_0_arr = np.array([M1,M2,M3,M4,M5,M6,M7,M8,M9])

# n x n matrix of initial fluxes
flux_0_mat = np.zeros((n_boxes,n_boxes))

# Define fluxes (Gt/year)
F_12 = 90
flux_0_mat[0][1] = 90 # Flux from Atmosphere to Surface Ocean

F_21 = 90
flux_0_mat[1][0] = 90 # Flux from Surface Ocean to Atmosphere

F_71 = 55 
flux_0_mat[6][0] = 55 # Flux from Deep Ocean to Atmosphere

F_57 = 55 
flux_0_mat[4][6] = 55 # Flux from Short-lived Biota to Deep Ocean

F_15 = 110 
flux_0_mat[0][4] = 110 # Flux from Atmosphere to Short-lived Biota

F_51 = 55 
flux_0_mat[4][0] = 55 # Flux from Short-lived Biota to Atmosphere

F_72 = 0 
flux_0_mat[6][1] = 0 # Flux from Deep Ocean to Surface Ocean

# Define rate constants (k values)
def calc_rate_const(Mi0,Fi0):
  n_boxes=len(Mi0)
  rate_constant = np.zeros((n_boxes, n_boxes))

  for c in range(n_boxes):
    for r in range(n_boxes):
      if (Mi0[r] != 0):
        rate_constant[r,c] = Fi0[r,c]/Mi0[r]

  return rate_constant

rate_constants = calc_rate_const(mi_0_arr, flux_0_mat)

# define ODEs
def nODEs(t,m):
  mdot = np.zeros(n_boxes)

  for i in range(n_boxes):
    for j in range(n_boxes):
      Fij = rate_constants[i][j] * m[i]
      

# def nineODEs(t,m):

print(rate_constants)
print(mi_0_arr)
print(flux_0_mat)