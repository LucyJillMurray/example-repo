import math
side1 = int(input("Enter first triangle side: "))
side2 = int(input("Enter second triangle side: "))
side3 = int(input("Enter third triangle side: "))


s = (side1 + side2 + side3)/2 
area = math.sqrt(s*(s-side1)*(s-side2)*(s-side3))
print(area)