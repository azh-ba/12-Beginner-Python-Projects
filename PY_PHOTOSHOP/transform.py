from image import Image
import numpy as np

def brighten(image, factor):
    """Make each channel higher by some amount.
    Factor is a value > 0, indicates how much brighteness the image is.
    (< 1 = darken, > 1 = brighten).
    """
    pass

def adjust_contrast(image, factor, mid):
    """Adjust the contrast by increasing the difference from the user-defined midpoint by factor amount."""
    pass

def blur(image, kernel_size):
    """Kernel size is the number of pixels to take into account when applying the blur.
    (example: kernel_size = 3 --> neightbors to the left/right, top/bottom, and diagonals)
    Kernel size should always be an *odd* number.
    """
    pass

def apply_kernel(image, kernel):
    """Kernel should be a 2D array that represents the kernel. Assume that the kernel is square.
    (example: sobel * kernel (detecting horizontal edges) is: 
        [1 0 -1]
        [2 0 -2]
        [1 0 -1] )
    """
    pass

def combine_images(image1, image2):
    """Combine two images using the squared sum of squares: value = sqrt(value1 ** 2, value2 ** 2).
    Size of image1 and image2 must be the same.
    """
    pass

if __name__ == '__main__':
    lake = Image(filename = 'lake.png')
    city = Image(filename = 'city.png')