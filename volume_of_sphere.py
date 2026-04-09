import math

def calculate_volume_of_sphere(radius):
    # Formula: (4/3) * pi * r^3
    volume = (4/3) * math.pi * (radius ** 3)
    return volume

# Compute and print the volume for radii 30 and 40
radius_1 = 30
radius_2 = 40

print(f"The volume of a sphere with radius {radius_1} is {calculate_volume_of_sphere(radius_1)}")
print(f"The volume of a sphere with radius {radius_2} is {calculate_volume_of_sphere(radius_2)}")