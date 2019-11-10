import numpy as np
from scipy import signal

Ac = np.array([[0,1,0],[ 3,0,1 ],[ 0,1,0]])
Bc = np.array([[1],[1],[3]])
Cc = np.array([[0,1,0]])
Dc = np.zeros((1,1))

print("A:")
print(Ac)
print("\n")

print("B:")
print(Bc)
print("\n")

print("C:")
print(Cc)
print("\n")

print("D:")
print(Dc)
print("\n")

m1 = Cc.shape[0]
n1 = Cc.shape[1]
n_in = Bc.shape[1]

## Make A Augmented Model
Ae = np.eye(n1+m1,n1+m1)
Ae[0:n1,0:n1] = Ac
Ae[n1:n1+m1,0:n1] = np.matmul(Cc,Ac)

## Make B Augmented Model
Be = np.zeros(((n1+m1),n_in))
Be[0:n1,:] = Bc
Be[n1:n1+m1,:] = np.matmul(Cc,Bc)
print(Be)

## Make B Augmented Model
Ce = np.zeros((m1,n1+m1))
Ce[:,n1:n1+m1] = np.eye(m1,m1)
print(Ce)

sys = signal.StateSpace(Ac,Bc,Cc,Dc,dt=1)
AugSys = signal.StateSpace(Ae, Be, Ce, dt = 1)

# print(sys)
# print(AugSys)

import matplotlib.pyplot as plt
t,result = signal.dstep(sys)
# print(result)
plt.plot(t,result[0])
plt.show()
