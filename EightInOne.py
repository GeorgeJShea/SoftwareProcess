from math import pi
from pathlib import Path
import unittest
#________________________________________________________________________________________
# Name: George Shea     ßeta
# Date Created: 20/9/21
# Date Modified 20/9/21
# I refuse to have 8 files
# Version 1.0
#________________________________________________________________________________________

path = Path().absolute()

fileNames = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight"]
def StartUp():
    print("Loading...")
    counter = 0
    for x in files:
        f = open(str(fileNames[counter] + ".py"), "w")
        f.writelines(files[counter])
        #f.close()
        print(counter)
        counter = counter + 1

eaulTriangleMethod = '''
from math import sqrt
def main():
    a = float(input("Enter Triangle's Leg: "))

    area = (sqrt(3)/4) * a**2
    print("Area: ", area)
    
if __name__ == '__main__':
    main()
'''

cubeoidMethod = '''
def main():
    a = float(input("Enter Cube's Leg one: "))
    b = float(input("Enter Cube's Leg two: "))
    c = float(input("Enter Cube's Leg three: "))

    area = a * b * c
    surface = 2*a*b + 2*a*c + 2*c*b
    print("Area: ", area, "  Surface: ", surface)

if __name__ == '__main__':
    main()
'''

trapizoidMethod = '''
def main():
    a = float(input("Enter Trapizoid's Top Base: "))
    b = float(input("Enter Trapizoid's Bottom Base: "))
    height = float(input("Enter Trapizoid's Height: "))

    area = (a+b/2) * height
    print("Area: ", area)

if __name__ == '__main__':
    main()
'''

triangleMethod = '''
from math import sqrt
def main():
    a = float(input("Enter Triangle's Leg one: "))
    b = float(input("Enter Triangle's Leg two: "))
    c = float(input("Enter Triangle's Leg three: "))
    p = a + b + c
    area = sqrt(p* (p-a) * (p - b) * (p-c))
    print("Area: ", area)

if __name__ == '__main__':
    main()
'''

cubeMethod = '''
def main():
    leg = float(input("Enter Cubes's Leg: "))
    print("Surface Area: ", 6 * leg**2, "Area: ", leg**3)
    
if __name__ == '__main__':
    main()
'''

coneMethod = '''
from math import pi
from math import  sqrt
def main():
    radi = float(input("Enter Cone's Radius: "))
    hieght = float(input("Enter Cone's Height: "))
    surface = (pi * radi) * (radi + sqrt((hieght**2) + (radi**2)))
    area = pi * (radi**2) * (hieght/3)
    print("Surface Area: ", surface, "Area: ", area)

if __name__ == '__main__':
    main()
'''

cylinderMethod = '''
from math import pi
def main():
    radi = float(input("Enter Cylinders's Radius: "))
    hieght = float(input("Enter Cylinders's Height: "))
    surface = 2 * pi * hieght + 2 * pi * radi ** 2
    area = pi * hieght * radi ** 2
    print("Surface Area: ", surface, "Area: ", area)
    
if __name__ == '__main__':
    main()
'''

sphereMethod = '''
from math import pi
def main():
    radi = float(input("Enter Sphere's Radius: "))
    result = (4/3) * pi * (radi**3)
    print("Resualt Rounded: ", round(result))

if __name__ == '__main__':
    main()
'''

sphereMethodTest = ''''''


files = [sphereMethod, cylinderMethod, coneMethod, cubeMethod, triangleMethod, trapizoidMethod, cubeoidMethod, eaulTriangleMethod]
filesTests = [sphereMethodTest]
def main():
    print("I refuse yet i dont refuse: ")
    StartUp()
    import Zero
    import One
    import Two
    import Three
    import Four
    import Five
    import Six
    import Seven
    print("=====================================================")
    print("Shapes Calculator")
    print("1 Sphere || 2 Cylinder || 3 Cone || 4 Cube")
    print("5 Triangle || 6 Trapizoide || 7 Cubeoid || 8 Equal Triangle")
    print("type anything else to exit")
    value = int(input("   "))
    if(value == 1):
        Zero.main()
    elif(value == 2):
        One.main()
    elif(value == 3):
        Two.main()
    elif (value == 4):
        Three.main()
    elif(value == 5):
        Four.main()
    elif(value == 6):
        Five.main()
    elif(value == 7):
        Six.main()
    elif(value == 8):
        Seven.main()
    else:
        "no"
        main()
    main()

if __name__ == '__main__':
    main()
