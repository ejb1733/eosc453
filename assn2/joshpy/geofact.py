import numpy as np

def geo_fact(zone,t, period=31536000):

    if zone == 0 or zone == 5:
        gf = 0.18602088*np.cos(((2*np.pi*t)/period) + (np.pi*0.9726)+(zone*np.pi))+0.18321732
        #gf = np.exp(.9155*np.sin((2*np.pi*t) / (period)-np.pi )-1.745028567)- 0.06704
    if zone == 1 or zone == 4:
        #gf = np.exp(0.075*np.sin((2*np.pi*t) / (period)-np.pi )+0.6085147897)- 1.61
        gf = 0.13720074*np.cos(((2*np.pi*t)/period) + (np.pi*0.9726)+((zone+1)*np.pi))+0.23004537
    if zone == 2 or zone == 3:
        gf = 0.04984369*np.cos(((2*np.pi*t)/period) + (np.pi*0.9726)+(zone*np.pi))+0.28175096
    return gf