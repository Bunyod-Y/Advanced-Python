# import numpy as np
# import matplotlib.pyplot as plt
# x = np.linspace(0, 4 * np.pi, 100)
# cosx = np.cos(x) # find cos(x) for above 100 points
# plt.plot(x,cosx) # plot (x, sin(x))
# plt.xlabel("Time") # label for x axis
# plt.ylabel("Amplitude") # label for y axis
# plt.title('Sine wave') # title
# plt.xlim([0, 4*np.pi]) # x-axis display range
# plt.ylim([-3, 3]) # y-axis display range
# plt.show() # to show the plot on the screen

# import numpy as np
# a=np.arange(1,10) # last element i.e. 10 is notincluded in result
# print(a) # [1 23 4 5 6 7 89]
# print(a.shape) # (9,) i.e. total 9 entries

# b=np.arange(1,10,2) # print 1to 10 with the spacing of 2
# print(b) # [1 35 7 9]
# print(b.shape) # (5,) i.e. total 9 entries

# c=np.arange(10, 2,-2) # last element 2 is not includedin result self
# print(c) # [10 8 6 4]


import numpy as np

a=np.array([1, 8, 2]) 
print(a) #[1 8 2]
print(np.shape(a)) #(3,)

b=np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])
print(np.shape(b))
