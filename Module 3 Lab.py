# Author: Zaineb Daisy Bonilla
# Date: 10/23/2022
# Version: 1.0
# Module 3 LAB
# Purpose:Creating Python program solutions for lab 3's following seven problems

import math

#question 1
print("Hello World!")

#question 2 & question 3
name = input("enter your name:")
if name == "Zaineb" or name == "Dr.Tovar":
    print("Welcome, "+name+"! It was a pleasure meeting you.")
else:
    print("Unable to great, User was not found.")

#question 4
radius = float (input ("To find the area enter the radius of the circle: "))
area = math.pi * radius * radius
print("Good work! The area of the circle is: {0}".format (area))

#question 5
print("To calculate the MPG or miles per gallon for your car enter the following") #This dalculates the Miles Per Gallon
miles_driven = input("Enter miles driven:") #This obtains the miles driven from the user
miles_driven = float(miles_driven) #This converts text entered to a floating point number
gallons_used = input("Enter gallons used:") #This obtains the gallons used from the user
gallons_used = float(gallons_used) #This converts the text entered into a floating point number
mpg = miles_driven / gallons_used #This is used to calculate and print the answer
print("Miles per gallon:", mpg) #This prints the answer

#question 6
print("To convert degrees Fahrenheit to degrees Celsius")
Fahrenheit = float(input("Enter the temperature in Fahrenheit:"))
Celsius = (Fahrenheit -32) * 5/9
print(Fahrenheit, "degrees Fahrenheit is =", Celsius, "degrees Celsius")

#question 7
def get_day_name(day): #this defines the dates
    if day == 0:
        return "Sunday"
    elif day == 1:
        return "Monday"
    elif day == 2:
        return "Tuesday"
    elif day == 3:
        return "Wednesday"
    elif day == 4:
        return "Thursday"
    elif day == 5:
        return "Friday"
    else:
        return "Saturday"

start = int(input("What is your starting day number? ")) #prompts user to enter data
duration = int(input("What is the length of your stay? ")) #prompts user to enter data
day = (duration % 7) + start
print(get_day_name(day)) #this prints the answer


