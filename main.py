from PIL import Image

ASCII_RANGE = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

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
            group.append(round((max(r, g, b) + min(r, g, b)) / 2))

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

def get_ascii_character_list(avg: list):
    holder = []

    for row in range(len(avg)):
        group = []
        for column in range(len(avg[0])):
            char_num = round(avg[row][column] * ((len(ASCII_RANGE)-1) / 255))
            ascii_char = ASCII_RANGE[char_num]
            group.append(ascii_char)

        holder.append(group)
    return holder

def print_ascii_art(ascii_list: list):
    for row in range(len(ascii_list)):
        for column in range(len(ascii_list[0])):
            print(ascii_list[row][column], end='')
        print()

with Image.open("images/pineapple.jpg") as image:
    pixels = get_pixel_rgb_list(image)
    pixels = get_average_brightness_list(pixels)
    pixels = get_ascii_character_list(pixels)

    print_ascii_art(pixels)
