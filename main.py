from PIL import Image, ImageOps

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
            group.append(round((r + g + b) / 3, 0))

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
            group.append(round(0.21 * r + 0.72 * g + 0.07 * b))

        holder.append(group)
    return holder


def get_ascii_character_list(avg: list):
    holder = []

    for row in range(len(avg)):
        group = []
        for column in range(len(avg[0])):
            char_num = round(avg[row][column] * ((len(ASCII_RANGE) - 1) / 255))
            ascii_char = ASCII_RANGE[char_num]
            group.append(ascii_char)

        holder.append(group)
    return holder


def get_reverse_ascii_character_list(avg: list):
    holder = []

    for row in range(len(avg)):
        group = []
        for column in range(len(avg[0])):
            char_num = round(avg[row][column] * ((len(ASCII_RANGE) - 1) / 255))
            ascii_char = ASCII_RANGE[64 - char_num]
            group.append(ascii_char)

        holder.append(group)
    return holder


def print_ascii_art(ascii_list: list):
    for row in range(len(ascii_list)):
        for column in range(len(ascii_list[0])):
            print(ascii_list[row][column] * 2, end='')
        print()


def get_brightness_mode():
    print("(1. avg brightness 2. lightness 3. luminosity)")
    while True:
        try:
            mode = int(input("Pick a brightness mode: "))
        except ValueError:
            print("\033[31m Enter a NUMBER 1-3 \033[0m")
        else:
            if 3 >= mode >= 1:
                return mode
        print("\033[31m Number has to be between 1 and 3 \033[0m")


def get_contrast_mode():
    print("(1. normal 2. inverted)")
    while True:
        try:
            mode = int(input("Pick a contrast mode: "))
        except ValueError:
            print("\033[31m Enter a NUMBER 1 or 2 \033[0m")
        else:
            if 2 >= mode >= 1:
                return mode
        print("\033[31m Number has to be 1 or 2 \033[0m")

brightness_mode = get_brightness_mode()
contrast_mode = get_contrast_mode()

image = Image.open("images/pineapple.jpg")

pixels = get_pixel_rgb_list(image)

if brightness_mode == 1:
    pixels = get_average_brightness_list(pixels)
elif brightness_mode == 2:
    pixels = get_average_lightness_list(pixels)
else:
    pixels = get_average_luminosity_list(pixels)

if contrast_mode == 1:
    pixels = get_ascii_character_list(pixels)
else:
    pixels = get_reverse_ascii_character_list(pixels)

print_ascii_art(pixels)
