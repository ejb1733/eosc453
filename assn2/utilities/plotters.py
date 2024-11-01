import matplotlib.pyplot as plt

# Define function for plotting integrated time series
def plottr(X, Y, xlab, ylab, title, suptitle, N=6, x0=None, y0=None, xf=None, yf=None):
    
    # plottr() inputs:
    #       X (1D np.array):    1D numpy array of independent var
    #       Y (M x D np.array): M array(s) of dependent var (usually M=6 for 6 zonal equations)

    #       xlab (str): x-axis label
    #       ylab (str): y-axis label
    #       title (str): plot title
    #       suptitle (str): super title

    #       x0 (int): lower bound on independent var (usually time)
    #       y0 (int): lower bound on dependent var (usually temp)
    #       xf (int): upper bound on independent var (usually time)
    #       yf (int): upper bound on dependent var (usually temp)

    # plottr outputs:
    #       plot: matplotlib pyplot

    plot = plt.figure()

    plt.plot(X,Y)
    plt.xlabel(xlab), plt.ylabel(ylab)
    plt.title(title)
    plt.suptitle(suptitle)

    plt.show()

    return plot