# Import required modules
import numpy as np
import cv2


# Create a white canvas
def create_canvas(height, width, color):
    """
    Creates a canvas of height, width, and color
    :param color: List of RGB integer values [R, G, B]
    :return: numpy array representing 3-dimensional matrix of canvas
    """
    canvas = np.zeros([height, width, 3], dtype=np.uint8)
    # fill matrix with RGB values using slicing
    canvas[:, :] = color
    return canvas


# Display an image
def display_image(image, window_name):
    cv2.imshow(window_name, image)
    cv2.waitKey(0)


def load_image(filename):
    image = cv2.imread(filename, cv2.IMREAD_COLOR)
    return image


if __name__ == "__main__":
    # load color wheel, source: https://pixabay.com/illustrations/colour-wheel-chromatic-rainbow-1734867/
    color_wheel = load_image("color_wheel_640x640.jpg")

    # set up canvas
    height = 640
    width = 640
    white = [255, 255, 255]
    canvas = create_canvas(height, width, white)

    # stack canvas and color wheel together
    stacked_image = np.hstack((canvas, color_wheel))

    display_image(stacked_image, "Color Blender")
