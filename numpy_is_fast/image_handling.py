## Using NumPy for Image Manipulations and Physics Calculations ##
'''If you're manipulating images (e.g., rotations, scaling) or calculating physics 
(e.g., collision detection algorithms, particle systems), NumPy can significantly 
peed up these operations:'''

# Image Manipulations: 
'''Pygame surfaces can be converted to and from NumPy arrays. 
This allows you to use NumPy's fast array operations for image processing tasks.'''

import pygame
import numpy as np

## mini game simulation ##

# Initialize Pygame
pygame.init()

# Create a Pygame surface (e.g., 400x400 pixels)
width, height = 400, 400
surface = pygame.display.set_mode((width, height))

# Fill the surface with a red color
surface.fill((255, 0, 0))

# Convert the surface to a NumPy array
surface_array = pygame.surfarray.pixels3d(surface)

# Manipulate the array, for example, change half of the surface to blue
surface_array[:width//2, :] = [0, 0, 255]

# Update the display to see changes
pygame.display.flip()

# Keep the window open until closed by the user
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()



# Assuming you have a surface called 'surface'
# Convert Pygame surface to a NumPy array
surface_array = pygame.surfarray.pixels3d(surface)

# Perform operations on the array for fast manipulation
# For example, invert the colors
inverted_array = 255 - surface_array

# Convert back to a surface (if necessary)
surface = pygame.surfarray.make_surface(inverted_array)

# Physics Calculations: 
'''For games with custom physics calculations, using NumPy for vectorized operations 
on positions, velocities, or forces can make the computations faster.'''
# Example: Updating positions using velocity vectors
positions = np.array([[100, 200], [150, 300]])  # Example initial positions
velocities = np.array([[5, 5], [-3, 2]])  # Example velocities

# Update positions in a vectorized manner
positions += velocities

