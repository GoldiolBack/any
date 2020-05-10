import numpy as np
import matplotlib.pyplot as plt
import time

# start the timer to know how long the whole code lasts
start_time = time.time()

# the array that counts how many colors of each kind
num_colors = np.zeros((8, 1), dtype='int')

# define the array that contains the colors available
colors = np.ndarray((8, 3), dtype='int')
for color in range(colors.shape[0]):
    b = color % 2
    g = (np.trunc((color/2)%2)).astype('int')
    r = (np.trunc((color/4)%2)).astype('int')
    colors[color, :] = [r, g, b]

# creates random images (you can change this by your images, reading them with skimage.io.imread() function)
# these are 12 images of 32x32 pixels and 8 colors available
images = np.random.randint(low=0, high=2, size=(12, 32, 32, 3), dtype=int) 

# define a function to plot six of the images
def show_im(a, b, c, d, e, f):
    fig = plt.figure()
    ax1 = fig.add_subplot(231)
    ax2 = fig.add_subplot(232)
    ax3 = fig.add_subplot(233)
    ax4 = fig.add_subplot(234)
    ax5 = fig.add_subplot(235)
    ax6 = fig.add_subplot(236)
    ax1.imshow(a/a.max()) # divide by maximum to normalize image (avoid visualization problems sometimes)
    ax2.imshow(b/b.max())
    ax3.imshow(c/c.max())
    ax4.imshow(d/d.max())
    ax5.imshow(e/e.max())
    ax6.imshow(f/f.max())
    plt.show()

# plot the first six images
show_im(images[0], images[1], images[2], images[3], images[4], images[5])

# count how many colors each image have
# for every image, every row, and every column, compares each pixel with the colors we have, one by one
for i in range(images.shape[0]):
    for j in range(images.shape[1]):
        for k in range(images.shape[2]):
            for l in range(colors.shape[0]):
                if np.all(images[i, j, k] == colors[l]):
                    num_colors[l] += 1

# print the results
print('Total of pixels for each color:')
print('\tColor black: {}'.format(num_colors[0]))
print('\tColor blue: {}'.format(num_colors[1]))
print('\tColor green: {}'.format(num_colors[2]))
print('\tColor cyan: {}'.format(num_colors[3]))
print('\tColor red: {}'.format(num_colors[4]))
print('\tColor pink: {}'.format(num_colors[5]))
print('\tColor yellow: {}'.format(num_colors[6]))
print('\tColor white: {}'.format(num_colors[7]))

print('\nSum of all colors: {}'.format(np.sum(num_colors)))
print('Total of pixels of all images: {}'.format(images.shape[0]*images.shape[1]*images.shape[2]))

#print the time elapsed
print("\n--- %s seconds ---" % (time.time() - start_time))
