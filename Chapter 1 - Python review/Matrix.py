import numpy as np
from scipy.linalg import lu
a= np.mat('1, 2; 3,2; 2, 3') # define matrix
aT = np.transpose(a) # transposeof matrix 'a'
b=2*np.eye(3) # 2 *Identity matrix
c = b*a
l= lu(a)
print(l)