# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

plt.ion();
plt.figure();


# Define the grid
grid_length     = 5;    # cm
grid_width      = 5;    # cm
grid_spacing    = 1;  # cm  

grid_length_steps   = grid_length/1.25*200;
grid_width_steps    = grid_width/1.25*200;
grid_spacing_steps  = grid_spacing/1.25*200;

x_grid_marks = int(grid_length/grid_spacing);
y_grid_marks = int(grid_width/grid_spacing);

x = np.linspace(0,grid_length_steps,x_grid_marks);
x = np.floor(x);

y = np.linspace(0,grid_width_steps,y_grid_marks);
y = np.floor(y);
    
z = [[0 for j in range(int(x_grid_marks))] for i in range(int(y_grid_marks))]
   
for i in range(x_grid_marks):
    for j in range(y_grid_marks):
        z[i][j] = 2.0/(i+j+1)
    
x = np.array(x);
y = np.array(y);
z = np.array(z);

plt.pcolormesh(x/200*1.25,y/200*1.25,z)
plt.colorbar()

Z_interpolator = interpolate.RectBivariateSpline(x,y,z);
plt.figure();

x = np.linspace(0,grid_length_steps,x_grid_marks*20)
y = np.linspace(0,grid_width_steps,y_grid_marks*20)

z = [[0 for j in range(int(x_grid_marks*20))] for i in range(int(y_grid_marks*20))]

for i in range(x_grid_marks*20):
    for j in range(y_grid_marks*20):
        z[i][j] = Z_interpolator(x[i],y[j])[0][0]
        
x = np.array(x);
y = np.array(y);
z = np.array(z);

plt.pcolor(x/200*1.25,y/200*1.25,z)
plt.colorbar()
