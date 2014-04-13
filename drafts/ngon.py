import numpy as np
import matplotlib.pyplot as plt

def ngon(n):
    x = [np.sin(np.pi/n + (k*2*np.pi)/n) for k in range(n+1)]
    y = [-1*np.cos(np.pi/n + (k*2*np.pi)/n) for k in range(n+1)]
    return x,y
    
plt.plot(*ngon(5))
plt.axes().set_aspect('equal')
plt.savefig('test.pdf')
