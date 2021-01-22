
import numpy as np
import cv2


# Create a white canvas
def create_canvas(height, width, color):
    canvas = np.zeros([height, width, 3], dtype=np.uint8)
    # fill matrix with RGB values using slicing
    canvas[:, :] = color
    return canvas


# Display an image
def display_image(image, window_name):
    cv2.imshow(window_name, image)


# load from file
def load_image(filename):
    image = cv2.imread(filename, cv2.IMREAD_COLOR)
    return image


# mouse callback function
def on_click_color_wheel(event, x, y, flags, userdata):
    if event == cv2.EVENT_LBUTTONUP:
        # unpack userdata
        color_wheel, canvas, canvas_window_name = userdata

        # get and mix colors
        alpha_bgr = get_rgb_values(color_wheel, x, y)
        beta_bgr = get_rgb_values(canvas, 0, 0)
        new_bgr = mix_colors(alpha_bgr, beta_bgr)

        # fill canvas with new=\

        cv2.imshow(canvas_window_name, canvas)


def get_rgb_values(image, x, y):
    # y before x, since the image is [height, width, channels]
    return image[y, x]


def mix_colors(alpha, beta):
    # using dtype np.uint16 to prevent cutting off intermediate values over 255
    new_color = np.mean([alpha, beta], dtype=np.uint16, axis=0)
    return new_color.astype('uint8')


if __name__ == "__main__":
    # load color wheel, source: https://pixabay.com/illustrations/colour-wheel-chromatic-rainbow-1734867/
    color_wheel_image = load_image("color_wheel_640x640.jpg")

    # set up canvas
    height = 640
    width = 640
    white = [255, 255, 255]
    canvas_image = create_canvas(height, width, white)

    color_wheel_window_name = "Color Wheel"
    canvas_window_name = "Canvas"

    display_image(canvas_image, canvas_window_name)
    display_image(color_wheel_image, color_wheel_window_name)

    userdata = (color_wheel_image, canvas_image, canvas_window_name)

    cv2.setMouseCallback(color_wheel_window_name, on_click_color_wheel, userdata)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
