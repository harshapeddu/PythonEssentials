#python fundamentals2 -- harshapeddu -- 2ndupdate
# coding: utf-8

# In[17]:


# this program is to calculate the BMI for given weight in kgs and height in mtrs
W = int(input('enter the weight in KG: '))
H = float(input('enter the height in feet: '))
#convert feet into mtrs
HM = float(0.3048*H)
#caliculating BMI
BMI = float(W/(HM**2))
print('your bmi is : ', round(BMI,2))


# In[26]:


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


# In[18]:


# this is to convert the given number into years, months and days
x = int(input('enter the number :'))
years = int(x/365)
print('number of years : ', years)
d = x%365 
months = int((d)/30)
print('number of months :', months)
days = d%30
print('number of days :', days)


# In[31]:


#this program is to calculate the area of the triangle with 3 sides given
A = int(input('enter the length of side a: '))
B = int(input('enter the length of side b: '))
C = int(input('enter the length of side c: '))
#to find the half perimeter
P = float((A+B+C)/2)

print('the value of half perimeter is :', P)

#Area of the triangle

import math

Area = float(math.sqrt(P*(P-A)*(P-B)*(P-C)))

print('The area of the triangle :', Area)


# In[32]:


x = int(input('enter the number :'))
mins = int(x/60)
print('number of mins : ', mins)
secs = x%60 
print('number of seconds :', secs)

