from PIL import Image

def get_pixel_rgb_list(img):
    holder = []
    for row in range(image.height):
        group = []
        for column in range(image.width):
            group.append(image.getpixel((column, row)))

        holder.append(group)
    return holder


def get_average_brightness_list(rgb: list):
    holder = []

    for row in range(len(rgb)):
        group = []
        for column in range(len(rgb[0])):
            r, g, b = rgb[row][column]
            group.append(round((r + g + b)/3, 0))

        holder.append(group)
    return holder

def get_average_lightness_list(rgb: list):
    holder = []

    for row in range(len(rgb)):
        group = []
        for column in range(len(rgb[0])):
            r, g, b = rgb[row][column]
            group.append(round(max(r, g, b) + min(r, g, b) / 2))

        holder.append(group)
    return holder

def get_average_luminosity_list(rgb: list):
    holder = []

    for row in range(len(rgb)):
        group = []
        for column in range(len(rgb[0])):
            r, g, b = rgb[row][column]
            group.append(round(0.21*r + 0.72*g + 0.07*b))

        holder.append(group)
    return holder


with Image.open("images/pineapple.jpg") as image:
    pixels = get_pixel_rgb_list(image)
    pixels = get_average_brightness_list(pixels)

    print(pixels)



