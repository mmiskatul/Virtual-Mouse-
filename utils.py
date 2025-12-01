import numpy as np   


def get_angle(a,b,c): 
    radians = np.arctan2(c[1]-b[1],c[0]-b[0])-np.arctan2(a[1]-b[1],a[0]-b[0]) 
    angle =np.abs(np.degrees(radians)) 
    return angle 