#!/usr/bin/python

radius = float(input ("enter the value of radius:"))
PI = 3.14
if radius > 0:
    area = PI * radius * radius
    print('The area of circle is %0.3f' %area)
else:
    print('The radius entered is negative hence no area can be computed')
