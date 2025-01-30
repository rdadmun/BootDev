def hex_to_rgb(hex_color):
    if is_hexadecimal(hex_color) == True and len(hex_color) == 6:
        r = int(hex_color[:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:], 16)
        return r, g, b
    else:
        raise Exception("not a hex color string")