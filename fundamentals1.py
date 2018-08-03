#This is a demo line
#This is my first set of python programs
#this is written for python programming practice
# coding: utf-8

# In[1]:


a = input('enter value of a: ')
b = input('enter value of b: ')
c = int(a)+int(b)
print('the sum of two numbers is :',c)


# In[1]:


# This program calculates the simple intrest for the given amount, time, and intrest rate
print('this is to caliculate the simple intrest of the given amount')
P = float(input('enter the principle amount : '))
T = float(input('enter the time in years : '))
R = float(input('enter the rate of intrest : '))
SI = (P*T*R)/100
print('the simple intrest for the amount {0} for the time {1} years and the intrest {2} is :'.format(P, T, R), SI)


# In[16]:


print('this is to calculate the area of the rectangle')
L = float(input('enter the length of the rectangle: '))
B = float(input('enter the bredth of the rectangle: '))
P =L*B
print('the area of the rectangle is ',P)


# In[14]:


#this calculates the area of the circle
import math
R = int(input('enter the value for the radius'))
A = math.pi *R*R
print('Area of circle is : ', A)


# In[2]:


#this program is to calculate the area of the triangle with 3 sides given
A = int(input('enter the length of side a: '))
B = int(input('enter the length of side b: '))
C = int(input('enter the length of side c: '))
#to find the half perimeter
P = float((A+B+C)/2)

print('the value of half perimeter is :', P)

#Area of the triangle

import math

Area = math.sqrt(P*(P-A)*(P-B)*(P-C)) 

print('The area of the triangle with sides {0},{1},{2} is :'.format(A, B, C), Area)


# In[ ]:


# this program is to calculate the BMI for given weight in kgs and height in mtrs
W = int(input('enter the weight in KG: '))
H = float(input('enter the height in feet: '))
#convert feet into mtrs
HM = float(0.3048*H)
#caliculating BMI
BMI = float(W/(HM**2))
print('your bmi is : ',BMI)


# In[4]:


import math
print(math.sqrt(36*(4)*(4)*(4)))

