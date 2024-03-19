from image import Image
import numpy as np

def adjust_brightness(image, factor):
    """Make each channel higher by some amount.
    Factor is a value > 0, indicates how much brighteness the image is.
    (< 1 = darken, > 1 = brighten).
    """
    # get x, y pixels of image, & number of channels
    x_pixel, y_pixel, num_channels = image.array.shape

    # make an empty copy of the image
    new_image = Image(x_pixels = x_pixel, y_pixels = y_pixel, num_channels = num_channels)

    # non-vectorized
    for x in range(x_pixel):
        for y in range(y_pixel):
            for c in range(num_channels):
                new_image.array[x, y, c] = image.array[x, y, c] * factor
    return new_image


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

    """Adjust_brightness() --> brighter lake."""
    # bright_lake_image = adjust_brightness(lake, 1.7)
    # bright_lake_image.write_image('bright_lake_image.png')

    """Adjust_brightness() --> darker lake."""
    dark_lake_image = adjust_brightness(lake, 0.3)
    dark_lake_image.write_image('dark_lake_image.png')