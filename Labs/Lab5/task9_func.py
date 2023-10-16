# Write a function that computes the volume of a sphere given its radius.

import math

def sphere_volume(r):
    if r < 0:
        return "Radius cannot be negative."
    v = (4/3) * math.pi * (r**3)
    return v

r = float(input())
result = sphere_volume(r)
print(result)