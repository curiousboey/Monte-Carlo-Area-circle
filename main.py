import matplotlib.pyplot as plt
import numpy as np

x= [-1, 1, 1, -1, -1]
y= [-1, -1, 1, 1, -1]

r=1
t= np.arange(0,2*np.pi, 0.01)
x2 = r*np.sin(t)
y2 = r*np.cos(t)
plt.plot(x,y)
plt.plot(x2,y2)

x3 = np.random.uniform(-1, 1, 10000)
y3 = np.random.uniform(-1,1,10000)
x4= []
y4= []
x5= []
y5= []

for x_point in range(10000):
    sum= x3[x_point]**2 + y3[x_point]**2
    if  sum < 1:
        x4.append(x3[x_point])
        y4.append(y3[x_point])
    else:
        x5.append(x3[x_point])
        y5.append(y3[x_point])
plt.scatter(x4,y4)
plt.scatter(x5,y5)
plt.show()

actual_area= np.pi*1
area_monte= np.size(x4)/np.size(x5)
print("actual area= ", actual_area)
print("area by monte carlo= ", area_monte)