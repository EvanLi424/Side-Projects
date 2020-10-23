#Data Source: Satellite Image from WIFIRE Project

%matplotlib inline
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt
import imageio

from skimage import data

photo_data = imageio.imread('./wifire/sd-3layers.jpg')


#Standardize all pixels
#photo_data = misc.imread('./wifire/sd-3layers.jpg')
photo_data[150, 250] = 0
plt.figure(figsize=(10,10))
plt.imshow(photo_data)


#Changing colors in range
photo_data = imageio.imread('./wifire/sd-3layers.jpg')

photo_data[200:800, :] = photo_data[200:800, :] * 0.5
plt.figure(figsize=(10,10))
plt.imshow(photo_data)

photo_data = imageio.imread('./wifire/sd-3layers.jpg')

photo_data[:,:, 0] = 0
#photo_data[:,:, 1] = 0
photo_data[:,:, 2] = 0

plt.figure(figsize=(20,20))
plt.imshow(photo_data)


#Choose low value pixels
photo_data = imageio.imread('./wifire/sd-3layers.jpg')
print("Shape of photo_data:", photo_data.shape)
low_value_filter = photo_data < 200
print("Shape of low_value_filter:", low_value_filter.shape)


#Picking out low value pixels
# import random
plt.figure(figsize=(10,10))
plt.imshow(photo_data)
photo_data[low_value_filter] = 0
plt.figure(figsize=(10,10))
plt.imshow(photo_data)


#Masking image
total_rows, total_cols, total_layers = photo_data.shape
print("photo_data = ", photo_data.shape)

X, Y = np.ogrid[:total_rows, :total_cols]
print("X = ", X.shape, " and Y = ", Y.shape)

center_row, center_col = total_rows / 2, total_cols / 2
#print("center_row = ", center_row, "AND center_col = ", center_col)
#print(X - center_row)
#print(Y - center_col)
dist_from_center = (X - center_row)**2 + (Y - center_col)**2
#print(dist_from_center)
radius = (total_rows / 2)**2
#print("Radius = ", radius)
circular_mask = (dist_from_center > radius)
#print(circular_mask)
print(circular_mask[1500:1700,2000:2200])


#Circular mask
photo_data = imageio.imread('./wifire/sd-3layers.jpg')
photo_data[circular_mask] = 0
plt.figure(figsize=(20,20))
plt.imshow(photo_data)


#Targeting height of topography
photo_data = imageio.imread('./wifire/sd-3layers.jpg')
red_mask   = photo_data[:, : ,0] < 150
print(red_mask)
photo_data[red_mask] = 0
plt.figure(figsize=(15,15))
plt.imshow(photo_data)


#Emphasizing slope of topography
photo_data = imageio.imread('./wifire/sd-3layers.jpg')
green_mask = photo_data[:, : ,1] < 150

photo_data[green_mask] = 0
plt.figure(figsize=(15,15))
plt.imshow(photo_data)


#Highlighting mountain aspects 
photo_data = imageio.imread('./wifire/sd-3layers.jpg')
blue_mask  = photo_data[:, : ,2] < 150

photo_data[blue_mask] = 0
plt.figure(figsize=(15,15))
plt.imshow(photo_data)


#Applying Gaussian Blur
image = imageio.imread('./wifire/sd-3layers.jpg')
image[:,:, 0] = 0
image[:,:, 1] = 0
#photo_data[:,:, 2] = 0
#plt.figure(figsize=(20,20))
#plt.imshow(image)
import numpy as np
#print("before:")
#print(image[1500:1515,2500:2515, 2])
#print()
kernel = np.array([[.0357, 0.1429, .0357], [0.1429, 0.2857, 0.1429], [.0357, 0.1429, .0357]])

def gblurB(image):
    w = 1500
    x = 1503
    z = 2500
    y = 2503
    a = 1501
    b = 2501
    while True:
        new = np.multiply(kernel, image[w:x, z:y, 2])
        image[a, b, 2] = np.sum(new)
        z += 1
        y += 1
        b += 1
        if b == 3000:
            w += 1
            x += 1
            z = 2500
            y = 2503
            a += 1
            b = 2501
        if a == 2000:
            break

gblurB(image)
plt.figure(figsize=(20,20))
plt.imshow(image)