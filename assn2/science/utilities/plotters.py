import matplotlib.pyplot as plt

# Define function for plotting integrated time series
def plottr(x0, y0, xf, yf, xlab, ylab, X, Y, N=6):
    # plottr inputs:
    #       x0 (int): lower bound on independent var (usually time)
    #       y0 (int): lower bound on dependent var (usually temp)
    #       xf (int): upper bound on independent var (usually time)
    #       yf (int): upper bound on dependent var (usually temp)
    #       xlab (str): x-axis label
    #       ylab (str): y-axis label
    #
    #       X (1D np.array):    1D numpy array of independent var
    #       Y (M x D np.array): M array(s) of dependent var (usually M=6 for 6 zonal equations)

    # plottr outputs:
    #       plot: matplotlib pyplot

    plot = plt.plot(X,Y)
    plot.xlabel(xlab), plot.ylabel(ylab)

    return plot