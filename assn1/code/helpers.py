import numpy as np
import constants
import time

from emissions import emissions
from emissions import modified_emissions

# Define a function to calculate rate constants k_ij
def calc_rate_const(Mi0,Fi0):

    # The inputs to the function are:
    #         Mi0: a list of our boxes' initial masses
    #         Fi0: a 9 x 9 matrix of our boxes' fluxes F_ij

    # The output of the function is:
    #         rate_constant: a 9x9 matrix of our boxes' rate constants k_ij

    n_boxes = len(Mi0)
    # initialize our 9x9 rate constant output array
    rate_constant = np.zeros((n_boxes, n_boxes))

    for c in range(n_boxes):
        for r in range(n_boxes):
            # for each flux F_cr,
            # calculate the according rate constant
            if (Mi0[r] != 0):
              rate_constant[r,c] = Fi0[r,c]/Mi0[r]
    return rate_constant

# define our rate constant matrix for use in other files
rate_constants_nineboxes = calc_rate_const(Mi0=constants.Mi0_nineboxes,Fi0=constants.Fi0_nineboxes)

# Define a function to return n ODEs in accordance with our input-output flux model
def ODEs_nineboxes(t,M):
  # define the 
  n = len(M)
  ODEs = np.zeros(n)
  for r in range(n):
      ODEs[r] = -np.sum(M[r]*rate_constants_nineboxes[r,:]) + (rate_constants_nineboxes[:,r] @ M)

  if constants.FORCING:
     ODEs[0] = ODEs[0] + emissions(t)

  if constants.MODIFIED_EMISSIONS:
      ODEs[0] = ODEs[0] + modified_emissions(t)

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

        k1 = np.array([h * val for val in fxy(x,y)]) #evaluate function fxy; depending on equation, k1 can be complex; this is why we make Y & y 

        y += (k1)
        x += h
        X[ii+1] = x 
        Y[ii+1,:] = y

    # record end time of euler to print time elapsed in the function 
    end = time.time()
    print('Euler Time Elapsed: ' + str('%.3f'%(end - start)) + ' seconds')

    return X, Y
    #Constants, Integration time, time steps and initial conditions: This information could be contained in a separate input file that you call