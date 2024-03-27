# Sasha G and Manar A
# CSCE 160
# HW 4
# 2024 March 25

import math

# getArrays: Takes in two lists of the same length and asks the user to
# enter the coordinate pairs they want.
def getArrays(list1, list2):
    for i in range(len(list1)):
      #make coordinate numbers floats incase of decimal inputs 
        list1[i] = float(input("Enter x: "))
        list2[i] = float(input("Enter y: "))
        print("--------------")

# getDistance: Takes in two lists of the same length and calculates the distance using formula 
def calculateDistance(x, y, z):
    for i in range(len(x)):
        d = math.sqrt((x[i])**2 + (y[i])**2)
        z[i] = d

# sortParallelLists: Takes in two lists of the same lengths and sorts the coordinate pairs
# from nearest distance to origin to farthest distance from origin.
def sortParallelLists(x, y):
  z = [None] * len(x)

  calculateDistance(x, y, z)

  for current in range(len(x)):

      min = z[current]
      min_index = current

      min_x = x[current]
      min_y = y[current]

      for i in range(current+1, len(x)):
          if (z[i] < min):
              min = z[i]
              min_index = i

              min_x = x[i]
              min_y = y[i]

      z[min_index] = z[current]
      z[current] = min

      x[min_index] = x[current]
      y[min_index] = y[current]
      x[current] = min_x
      y[current] = min_y

def main():
    N = int(input("How many coordinates do you want to enter in? The number must be greater than or equal to 1: "))
    x = [None] * N
    y = [None] * N
    getArrays(x, y)
    sortParallelLists(x, y)

    print("Sorted:")
    for i in range(N):
      print("(", x[i], ",", y[i], ")", sep="")
      
main()