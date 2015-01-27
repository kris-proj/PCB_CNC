# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 13:28:08 2015

@author: 210078275
"""

import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
import serial
import time

simulate = 1;
probe = 1;

# Set up serial object
if(simulate == 0):
    ser = serial.Serial('COM2',115200)

# Constants
grid_x_length = 100 # mm
grid_y_length = 100 # mm

grid_increments = 5 # mm

z_travel_height = 1 # mm


# Define the grid
grid_x_marks = np.linspace(0,grid_x_length,grid_x_length/grid_increments+1)
grid_y_marks = np.linspace(0,grid_y_length,grid_y_length/grid_increments+1)

grid_x_marks = np.floor(grid_x_marks)
gird_y_marks = np.floor(grid_y_marks)

probe_heights = [[0 for j in grid_x_marks] for i in grid_y_marks]

if(probe == 1):  
    for i in range(len(grid_x_marks)):
        for j in range(len(grid_y_marks)):
            if(simulate):
                print('Command Z to '+str(z_travel_height))
                print('wait for OK')
                print('Commanding X'+(str(grid_x_marks[i])+' Y'+str(grid_y_marks[j])))
                print('wait for OK')
                print('Command probe')
                print('Wait for probe reply')
                print('Store the reply')
                probe_heights[i][j] = np.random.rand(1)[0];
            else:
                ser.write('G0 Z'+str(z_travel_height));
                waitforok();
                ser.write('G0 X'+str(grid_x_marks[i])+' Y'+str(grid_y_marks[j]))
                waitforok();
                ser.write('PROBE COMMAND')
                waitforprobe(i,j);

zeroing_factor = probe_heights[0][0]

for i in range(len(grid_x_marks)):
    for j in range(len(grid_y_marks)):
        probe_heights[i][j] = probe_heights[i][j] - zeroing_factor
        
x = np.array(grid_x_marks);
y = np.array(grid_y_marks);
z = np.array(probe_heights);

plt.ion()
plt.figure()

plt.pcolormesh(x,y,z)
plt.colorbar()
plt.draw()

z_interp = interpolate.RectBivariateSpline(x,y,z)

x_interpolated = np.linspace(0,grid_x_length,200)
y_interpolated = np.linspace(0,grid_y_length,200)

z_interpolated = [[0 for j in x_interpolated] for i in y_interpolated]

for i in range(len(x_interpolated)):
    for j in range(len(y_interpolated)):
        z_interpolated[i][j] = z_interp(x_interpolated[i],y_interpolated[j])[0][0]
        
x_interpolated = np.array(x_interpolated)
y_interpolated = np.array(y_interpolated)
z_interpolated = np.array(z_interpolated)


plt.figure()
plt.pcolormesh(x_interpolated,y_interpolated,z_interpolated)
plt.colorbar()
