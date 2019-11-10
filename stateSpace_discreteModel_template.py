import numpy as np
from scipy import signal

''' StateSpace Discrete Model
    Xm(k+1) = Am * Xm(k) + Bm * Um(k)
    Ym(k) = Cm * Xm(k) + Dm * Um(k)

    Snippet Program
                    [baris], [baris],[baris]
    Am = np.array([[0,1,0],[ 3,0,1 ],[ 0,1,0]])
    Bm = np.array([[1],[1],[3]])
    Cm = np.array([[0,1,0]])
    Dm = np.zeros((1,1))

    Example :
    Am = np.array([[0,1,0],[ 3,0,1 ],[ 0,1,0]])
    Bm = np.array([[1],[1],[3]])
    Cm = np.array([[0,1,0]])
    Dm = np.zeros((1,1))
'''

Am = np.array([[0,1,0],[ 3,0,1 ],[ 0,1,0]])
Bm = np.array([[1],[1],[3]])
Cm = np.array([[0,1,0]])
Dm = np.zeros((1,1))

sys = signal.StateSpace(Am,Bm,Cm,Dm,dt=1)
