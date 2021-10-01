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
        f = open(str(fileNames[counter] + ".py"), "a")
        f.writelines(files[counter])
        #f.close()
        print(counter)
        counter = counter + 1

eaulTriangleMethod = '''
from math import sqrt
def EqualTriangleMethod():
    a = float(input("Enter Triangle's Leg: "))

    area = (sqrt(3)/4) * a**2
    print("Area: ", area)
'''

cubeoidMethod = '''
def CubeoidMethod():
    a = float(input("Enter Cube's Leg one: "))
    b = float(input("Enter Cube's Leg two: "))
    c = float(input("Enter Cube's Leg three: "))

    area = a * b * c
    surface = 2*a*b + 2*a*c + 2*c*b
    print("Area: ", area, "  Surface: ", surface)
'''

trapizoidMethod = '''
def TrapizoidMethod():
    a = float(input("Enter Trapizoid's Top Base: "))
    b = float(input("Enter Trapizoid's Bottom Base: "))
    height = float(input("Enter Trapizoid's Height: "))

    area = (a+b/2) * height
    print("Area: ", area)
    
'''

triangleMethod = '''
from math import sqrt
def TriangleMethod():
    a = float(input("Enter Triangle's Leg one: "))
    b = float(input("Enter Triangle's Leg two: "))
    c = float(input("Enter Triangle's Leg three: "))
    p = a + b + c
    area = sqrt(p* (p-a) * (p - b) * (p-c))
    print("Area: ", area)
'''

cubeMethod = '''
def CubeMethod():
    leg = float(input("Enter Cubes's Leg: "))
    print("Surface Area: ", 6 * leg**2, "Area: ", leg**3)
'''

coneMethod = '''
from math import pi
from math import  sqrt
def ConeMethod():
    radi = float(input("Enter Cone's Radius: "))
    hieght = float(input("Enter Cone's Height: "))
    surface = (pi * radi) * (radi + sqrt((hieght**2) + (radi**2)))
    area = pi * (radi**2) * (hieght/3)
    print("Surface Area: ", surface, "Area: ", area)
'''

cylinderMethod = '''
from math import pi
def CylinderCalc():
    radi = float(input("Enter Cylinders's Radius: "))
    hieght = float(input("Enter Cylinders's Height: "))
    surface = 2 * pi * hieght + 2 * pi * radi ** 2
    area = pi * hieght * radi ** 2
    print("Surface Area: ", surface, "Area: ", area)
'''

sphereMethod = '''
from math import pi
def SphereCalc():
    radi = float(input("Enter Sphere's Radius: "))
    result = (4/3) * pi * (radi**3)
    print("Resualt Rounded: ", round(result))
'''

sphereMethodTest = ''''''


files = [sphereMethod, cylinderMethod, coneMethod, cubeMethod, triangleMethod, trapizoidMethod, cubeoidMethod, eaulTriangleMethod, eaulTriangleMethod]
filesTests = [sphereMethodTest]
def main():
    print("I refuse yet i dont refuse: ")
    StartUp()
    import Zero
    import Two




if __name__ == '__main__':
    main()
