#March 21 2025
import math

def degrees_to_radians(degrees):
    return degrees * math.pi / 180

degrees = float(input("Enter degrees: "))
radians = degrees_to_radians(degrees)
print(f"{degrees} degrees is {radians} radians")