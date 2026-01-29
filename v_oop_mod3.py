'''
v_oop_ mod3.py - is a oop intro program that declares the class Vehicle, the class Automobile inherits the traits of Vehicle

Proudly Engineered by Zachary Roberts, 28 JAN 2026
"Beats the heck out of walking there." 

Write a Python app that has the following classes:
A super class called Vehicle, which contains an attribute for vehicle type, such as car, truck, plane, boat, or a broomstick.
A class called Automobile which will inherit the attributes from Vehicle and also contain the following attributes:
year
make
model
doors (2 or 4)
roof (solid or sun roof).
Write an app that will accept user input for a car. The app will store "car" into the vehicle type in your Vehicle super class. 
The app will then ask the user for the year, make, model, doors, and type of roof and store thdata in the attributes above.
The app will then output the data in an easy-to-read and understandable format, such as this:
  Vehicle type: car
  Year: 2022
  Make: Toyota
  Model: Corolla
  Number of doors: 4
  Type of roof: sun roof
'''

class  Vehicle():
    def __int__(self, vehicle_type: str):
        self.vehicle_type: str = vehicle_type
        
class Automobile(Vehicle):
    def __init__(self, vehicle_type: str, year: str, make: str, model: str, doors: int, roof: str):
        super().__init__(vehicle_type)
        self.year: int = year
        self.make: str = make
        self.model: str = model
        if doors == 2 or doors == 4:
          self.doors: int = doors
        else:
            raise ValueError('Doors must equal 2 or 4.\n')
        if roof.lower() == 'solid' or roof.lower() == 'sun roof':
           self.roof: str = roof 
        else:
            raise ValueError('Roof must be "solid" or "sun roof\n')
        
year: int = int(input())
make: str = input()
model: str = input()
doors: int =int(input())
roof: str =(input())     
car = Automobile('car', year, make, model, doors, roof)
