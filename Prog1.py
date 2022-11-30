#Accept the length and width of the room in floating-point and compute the area of the room. Print area of the room including the units e.g. inch, meters, cms, feet, etc


length = float(input("Enter the lenght: "))
width = float(input("Enter the width: "))

area_feet = length * width
feet_inch_area = area_feet * 12
feet_meteres_area = area_feet * 0.3048
feet_cm = area_feet * 30.48


print("Area in feet: ",area_feet)
print("Area in inches: ",feet_inch_area)
print("Area in meters: ",feet_meteres_area)
print("Area in cm: ",feet_cm)
