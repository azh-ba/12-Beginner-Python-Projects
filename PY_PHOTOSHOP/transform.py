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

    # vectorized
    # new_image.array = image.array * factor

    return new_image


def adjust_contrast(image, factor, mid = 0.5):
    """Adjust the contrast by increasing the difference from the user-defined midpoint by factor amount."""
    # get x, y pixels of image, & number of channels
    x_pixel, y_pixel, num_channels = image.array.shape

    # make an empty copy of the image
    new_image = Image(x_pixels = x_pixel, y_pixels = y_pixel, num_channels = num_channels)

    # non-vectorized
    for x in range(x_pixel):
        for y in range(y_pixel):
            for c in range(num_channels):
                new_image.array[x, y, c] = (image.array[x, y, c] - mid) * factor - mid

    # vectorized
    # new_image.array = (image.array - mid) * factor + mid

    return new_image


def blur(image, kernel_size):
    """Kernel size is the number of pixels to take into account when applying the blur.
    (example: kernel_size = 3 --> neightbors to the left/right, top/bottom, and diagonals)
    Kernel size should always be an *odd* number.
    """
    # get x, y pixels of image, & number of channels
    x_pixel, y_pixel, num_channels = image.array.shape

    # make an empty copy of the image
    new_image = Image(x_pixels = x_pixel, y_pixels = y_pixel, num_channels = num_channels)

    # range of value that needed for calculation in each side
    neighbor_range = kernel_size // 2

    # find the average value of the current pixel by taking the sum of all pixels surrounding it, and divided by the square of the kernel size
    for x in range(x_pixel):
        for y in range(y_pixel):
            for c in range(num_channels):
                total = 0
                for x_i in range(max(x - neighbor_range, 0), min(x + neighbor_range + 1, x_pixel - 1)):
                    for y_i in range(max(y - neighbor_range, 0), min(y + neighbor_range + 1, y_pixel - 1)):
                        total += image.array[x_i, y_i, c]
                new_image.array[x, y, c] = total / (kernel_size ** 2)
    
    return new_image


def apply_kernel(image, kernel):
    """Kernel should be a 2D array that represents the kernel. Assume that the kernel is square.
    (example: sobel * kernel (detecting horizontal edges) is: 
        [1 0 -1]
        [2 0 -2]
        [1 0 -1] )
    """
    # get x, y pixels of image, & number of channels
    x_pixel, y_pixel, num_channels = image.array.shape

    # make an empty copy of the image
    new_image = Image(x_pixels = x_pixel, y_pixels = y_pixel, num_channels = num_channels)

    # range of value that needed for calculation in each side
    kernel_size = kernel.shape[0]
    neighbor_range = kernel_size  // 2

    for x in range(x_pixel):
        for y in range(y_pixel):
            for c in range(num_channels): 
                total = 0
                for x_i in range(max(x - neighbor_range, 0), min(x + neighbor_range + 1, x_pixel - 1)):
                    for y_i in range(max(y - neighbor_range, 0), min(y + neighbor_range + 1, y_pixel - 1)):
                        # find which value of the kernel this corresponds to
                        x_k = x_i + neighbor_range - x
                        y_k = y_i + neighbor_range - y
                        kernel_val = kernel[x_k, y_k]
                        total += image.array[x_i, y_i, c] * kernel_val
                new_image.array[x, y, c] = total
    
    return new_image


def combine_images(image1, image2):
    """Combine two images using the squared sum of squares: value = sqrt(value1 ** 2, value2 ** 2).
    Size of image1 and image2 must be the same.
    """
    # get x, y pixels of image, & number of channels
    x_pixel, y_pixel, num_channels = image1.array.shape

    # make an empty copy of the image
    new_image = Image(x_pixels = x_pixel, y_pixels = y_pixel, num_channels = num_channels)

    for x in range(x_pixel):
        for y in range(y_pixel):
            for c in range(num_channels): 
                new_image.array[x, y, c] = (image1.array[x, y, c] ** 2 + image2.array[x, y, c] ** 2) ** 0.5

    return new_image


if __name__ == '__main__':
    lake = Image(filename = 'lake.png')
    city = Image(filename = 'city.png')

    """adjust_brightness() --> brighter lake."""
    # bright_lake_image = adjust_brightness(lake, 1.7)
    # bright_lake_image.write_image('bright_lake_image.png')

    """adjust_brightness() --> darker lake."""
    # dark_lake_image = adjust_brightness(lake, 0.3)
    # dark_lake_image.write_image('dark_lake_image.png')

    """adjust_contrast() --> increase-contrast lake."""
    # increase_contrast_lake_image = adjust_contrast(lake, 2, 0.5)
    # increase_contrast_lake_image.write_image('increase_contrast_lake_image.png')

    """adjust_contrast() --> decrease-contrast lake."""
    # decrease_contrast_lake_image = adjust_contrast(lake, 0.7, 0.5)
    # decrease_contrast_lake_image.write_image('decrease_contrast_lake_image.png')

    """blur() --> blur city."""
    # blur_city_image = blur(city, 7)
    # blur_city_image.write_image('blur_city_image.png')

    """apply_kernel() --> sobel edge detection kernel on x and y axis."""
    # sobel_x_kernel = np.array([
    #     [1, 2, 1], 
    #     [0, 0, 0], 
    #     [-1, -2, -1]
    # ])
    # sobel_y_kernel = np.array([
    #     [1, 2, 1], 
    #     [2, 0, -2], 
    #     [-1, -2, -1]
    # ])
    # sobel_x = apply_kernel(city, sobel_x_kernel)
    # sobel_x.write_image('edge_x.png')
    # sobel_y = apply_kernel(city, sobel_y_kernel)
    # sobel_y.write_image('edge_y.png')

    """combine_image() --> edge detection filter (city)."""
    # sobel_x_kernel = np.array([
    #     [1, 2, 1], 
    #     [0, 0, 0], 
    #     [-1, -2, -1]
    # ])
    # sobel_y_kernel = np.array([
    #     [1, 2, 1], 
    #     [2, 0, -2], 
    #     [-1, -2, -1]
    # ])
    # sobel_x = apply_kernel(city, sobel_x_kernel)
    # sobel_y = apply_kernel(city, sobel_y_kernel)
    # sobel_xy = combine_images(sobel_x, sobel_y)
    # sobel_xy.write_image('edge_xy.png')