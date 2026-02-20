import math

# ---------------- CYLINDER ----------------
def cylinder_csa(radius, height):
    return 2 * math.pi * radius * height

def cylinder_tsa(radius, height):
    return 2 * math.pi * radius * (radius + height)

def cylinder_volume(radius, height):
    return math.pi * radius * radius * height


# ---------------- CONE ----------------
def cone_csa(radius, height):
    slant_height = math.sqrt(radius**2 + height**2)
    return math.pi * radius * slant_height

def cone_tsa(radius, height):
    slant_height = math.sqrt(radius**2 + height**2)
    return math.pi * radius * (radius + slant_height)

def cone_volume(radius, height):
    return (1/3) * math.pi * radius * radius * height


# ---------------- CUBOID ----------------
def cuboid_csa(length, width, height):
    return 2 * height * (length + width)

def cuboid_tsa(length, width, height):
    return 2 * (length*width + width*height + height*length)

def cuboid_volume(length, width, height):
    return length * width * height