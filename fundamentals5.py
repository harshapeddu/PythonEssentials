
# coding: utf-8

# In[4]:


# program to calculate the given number even or odd
a = int(input('enter the number :'))
if a%2 == 0:
    print('the number {0} is EVEN number'.format(a))
else:
    print('The number {0} is ODD number'.format(a))


# In[7]:


#program to calculate the given number has factor as 5
a = int(input('enter the number :'))
if a%5 == 0:
    print('the number {0} is indeed have 5 as factor '.format(a))
else:
    print('The number 5 is NOT a factor of {0} '.format(a))


# In[15]:


# Given 2 numbers num1 and num2 and to calculate which number is factor of which
num1 = int(input('Enter num1 :'))
num2 = int(input('Enter num2 :'))
if num1 >= num2:
    if num1%num2 == 0:
        print('{0} is factor of {1}'.format(num2,num1))
    else:
        print('{0} is NOT factor of {1}'.format(num2,num1))
else:
    if num2%num1 == 0:
        print('{0} is factor of {1}'.format(num1,num2))
    else:
        print('{0} is NOT factor of {1}'.format(num1,num2))
        
            


# In[43]:


# program to calculate the given year is LEAP year or not
a = int(input('enter the year : '))
if (a%4 == 0 and a%100 != 0) or a%400 == 0:
    print('LEAP YEAR')
else:
    print('NOT LEAP YEAR')


# In[47]:


#Program to calculate biggest of 3 numbers:
a = int(input('Enter the first number : '))
b = int(input('Enter the second number : '))
c = int(input('Enter the third number : '))
if a >= b and a >= c:
    print('{0} is the biggest'.format(a))
elif b >= c:
    print('{0} is the biggest'.format(b))
else:
    print('{0} is biggest'.format(c))
    


# In[51]:


a = int(input(' Enter any value (1-7) :'))
if a ==1:
    print('Monday')
elif a ==2:
    print('Tuesday')
elif a == 3:
    print('Wednesday')
elif a == 4:
    print('Thursday')
elif a == 5:
    print('Friday')
elif a ==6:
    print('Saturday')
elif a ==7:
    print('Sunday')
else:
    print('Wrong value. Enter 1-7 ')

