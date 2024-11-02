import matplotlib.pyplot as plt

# Define function for plotting integrated time series
def plottr(X, Y, xlab, ylab, title=None, suptitle=None, N=6, x0=None, y0=None, xf=None, yf=None, xline=None):
    
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

    if (xline != None):
        plt.axvline(x=xline, color='r', linestyle='--')

    if title != None: plt.title(title)
    if suptitle != None: plt.suptitle(suptitle)

    plt.xlabel(xlab), plt.ylabel(ylab)
    plt.ylim(y0,yf)

    labels = ['90\xb0S - 60\xb0S', '60\xb0S - 30\xb0S','30\xb0S - 0\xb0','0\xb0 - 30\xb0N','30\xb0N - 60\xb0N','60\xb0N - 90\xb0N', 'eruption year']

    # plt.legend(labels,
    #            loc='upper left',
    #            bbox_to_anchor=(1,1))
    
    plt.subplots_adjust(right=0.8)

    plt.show()

    return plot