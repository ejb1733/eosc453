import numpy as np
import constants
import time

from emissions import emissions
from emissions import modified_emissions

# Define rate constants k_ij; returns n x n matrix
def calc_rate_const(Mi0,Fi0):
    n_boxes = len(Mi0)

    rate_constant = np.zeros((n_boxes, n_boxes))
    rate_constant_test = np.zeros((n_boxes, n_boxes))
    for c in range(n_boxes):
        for r in range(n_boxes):
            if (Mi0[r] != 0):
              rate_constant[r,c] = Fi0[r,c]/Mi0[r]
    return rate_constant

rate_constants_onebox = calc_rate_const(Mi0=constants.Mi0_onebox,Fi0=constants.Fi0_onebox)
rate_constants_fourboxes = calc_rate_const(Mi0=constants.Mi0_fourboxes,Fi0=constants.Fi0_fourboxes)
rate_constants_nineboxes = calc_rate_const(Mi0=constants.Mi0_nineboxes,Fi0=constants.Fi0_nineboxes)

# rate_constants = calc_rate_const(Mi0=constants.Mi0_nineboxes, Fi0=constants.Fi0_nineboxes)

def ODEs_onebox(t,M):
  n = len(M)
  ODEs = np.zeros(n)
  
  for r in range(n):
      ODEs[r] = -np.sum(M[r]*rate_constants_fourboxes[r,:]) + (rate_constants_fourboxes[:,r] @ M)

  if constants.FORCING:
     ODEs[0] = ODEs[0] + emissions(t)

  if constants.FIRE:
      fire_gt = ODEs[1] * 0.96
      ODEs[1] = ODEs[1] - fire_gt
      ODEs[0] = ODEs[0] + fire_gt

  return ODEs

# Define a function to return n ODEs in accordance with our input-output flux model
def ODEs_nineboxes(t,M):
  # define the 
  n = len(M)
  ODEs = np.zeros(n)
  for r in range(n):
      ODEs[r] = -np.sum(M[r]*rate_constants_nineboxes[r,:]) + (rate_constants_nineboxes[:,r] @ M)

  if constants.FORCING:
     ODEs[0] = ODEs[0] + emissions(t)

  if constants.FIRE:
      long_biota_fire_gt = ODEs[5] * 0.96
      short_biota_fire_gt = ODEs[4] * 0.96
      ODEs[5] = ODEs[5] - long_biota_fire_gt
      ODEs[4] = ODEs[4] - short_biota_fire_gt
    #   print(f'LONGLIVE_0: {ODEs[1] + fire_gt}, LONGLIVE_f: {ODEs[1]}, ATM BEFORE V AFTER: {ODEs[0]} vs {ODEs[0] + fire_gt}')
      ODEs[0] = ODEs[0] + long_biota_fire_gt + short_biota_fire_gt

  if constants.MODIFIED_EMISSIONS:
      ODEs[0] = ODEs[0] + modified_emissions(t)

  return ODEs

def ODEs_fourboxes(t,M):
  n = len(M)
  ODEs = np.zeros(n)
  
  for r in range(n):
      ODEs[r] = -np.sum(M[r]*rate_constants_fourboxes[r,:]) + (rate_constants_fourboxes[:,r] @ M)

  if constants.FORCING: 
    ODEs[0] = ODEs[0] + emissions(t)

  if constants.MODIFIED_EMISSIONS: 
    ODEs[0] = ODEs[0] + modified_emissions(t)

  if constants.FIRE:
      fire_gt = ODEs[1] * 0.96
      ODEs[1] = ODEs[1] - fire_gt
      ODEs[0] = ODEs[0] + fire_gt

  return ODEs

#Define a function for the 4th order Runge-Kutta integration method and the ODEs to be solved.
def rk4(fxy, x0, xf, y0, N):

    # The inputs to the function are:
    #         fxy = the name of the function containing f(x,y) (e.g. oneode, twoode)
    #         xo,xf = initial and final values of the independent variable (integers or floats)
    #         yo = initial value of dependent variable at xo (numpy array)
    #         N = number of intervals to use between xo and xf (integer)

    # The outputs to the function are:
    #         X = numpy array containing values of the independent variable
    #         Y = the estimated dependent variable at each value of the independent variable
    #         --> this variable is a 1D numpy array if only one equation is solved
    #         --> it is an M-D numpy array [y1(x) y2(x) ... ] for multiple (M) equations

    # record start time of RK4 for measuring efficiency
    start = time.time()

    #compute step size and size of output variables
    if N < 2:
        N = 2 #set minimum number for N
    h = (xf - x0) / N
    print(f'STEP SIZE: {h}')
    X = np.zeros((N+1, 1))
    M = np.max(np.shape(y0))
    Y = np.zeros((N+1, M)) *1j #make complex by multiplying by 1j; this way can add complex values to this during integration

    #set initial conditions
    x = x0
    X[0] = x
    y = [complex(val) for val in y0]  #make complex
    Y[0,:] = y

    #begin computational loop
    for ii in range(N):

        k1 = np.array([h * val for val in fxy(x,y)]) #evaluate function fxy; depending on equation, k1-4 can be complex; this is why we make Y and y complex as well
        k2 = np.array([h * val for val in fxy(x+h/2, y+k1/2)])
        k3 = np.array([h * val for val in fxy(x+h/2, y+k2/2)])
        k4 = np.array([h * val for val in fxy(x+h, y+k3)])

        y += (k1 + 2*k2 + 2*k3 + k4) / 6.
        x += h
        X[ii+1] = x
        Y[ii+1,:] = y

    # record end time of RK4 to print time elapsed in the function 
    end = time.time()
    print('RK4 Time Elapsed: ' + str('%.3f'%(end - start)) + ' seconds')

    return X, Y
    #Constants, Integration time, time steps and initial conditions: This information could be contained in a separate input file that you call

def euler_method(fxy, x0, xf, y0, N):

    # The inputs to the function are:
    #         fxy = the name of the function containing f(x,y) (e.g. oneode, twoode)
    #         xo,xf = initial and final values of the independent variable (integers or floats)
    #         yo = initial value of dependent variable at xo (numpy array)
    #         N = number of intervals to use between xo and xf (integer)

    # The outputs to the function are:
    #         X = numpy array containing values of the independent variable
    #         Y = the estimated dependent variable at each value of the independent variable
    #         --> this variable is a 1D numpy array if only one equation is solved
    #         --> it is an M-D numpy array [y1(x) y2(x) ... ] for multiple (M) equations

    # record start time of euler for measuring efficiency
    start = time.time()

    #compute step size and size of output variables
    if N < 2:
        N = 2 #set minimum number for N
    h = (xf - x0) / N
    X = np.zeros((N+1, 1))
    M = np.max(np.shape(y0))
    Y = np.zeros((N+1, M)) *1j #make complex by multiplying by 1j; this way can add complex values to this during integration

    #set initial conditions
    x = x0
    X[0] = x
    y = [complex(val) for val in y0]  #make complex
    Y[0,:] = y

    #begin computational loop
    for ii in range(N):

        k1 = np.array([h * val for val in fxy(x,y)]) #evaluate function fxy; depending on equation, k1-4 can be complex; this is why we make Y and y 

        y += (k1)
        x += h
        X[ii+1] = x 
        Y[ii+1,:] = y

    # record end time of euler to print time elapsed in the function 
    end = time.time()
    print('Euler Time Elapsed: ' + str('%.3f'%(end - start)) + ' seconds')

    return X, Y
    #Constants, Integration time, time steps and initial conditions: This information could be contained in a separate input file that you call