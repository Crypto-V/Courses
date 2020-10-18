# Write a function that will calculate the volume of a sphere with the radius as a given attribute.


def vol(rad):
    pi = 3.14
    return (4 * pi * pow(rad, 3)) / 3


print(vol(2))
