
# coding: utf-8

# In[5]:


# this program is to calculate the BMI for given weight in kgs and height in mtrs
W = int(input('enter the weight in KG: '))
H = float(input('enter the height in feet: '))
#convert feet into mtrs
HM = float(0.3048*H)
#caliculating BMI
BMI = float(W/(HM**2))
print('your bmi is : ', round(BMI,2))
if BMI <= 18.5:
    print('Under Weight')
elif BMI > 18.5 and BMI <= 24.9:
    print('Healthy Weight')
elif BMI >=25 and BMI <= 30:
    print('Over Weight')
else:
    print('Obese')


# In[19]:


# Program to find the given number is Prime
a = int(input('Enter the number : '))                     #input value to find this number is Prime
i = 1                                                     #initiation variable and incrimentor
f = 0                                                     #factor count
while i <= a:                                             #While loop Start
    if a%i == 0:
        f += 1
    i += 1
if f == 2:
    print('Prime Number')
else:
    print('Not Prime Number')
    print('Factors : ', f)


# In[1]:


# Prime numbers upto 100 :
num = 1
while num <= 100:
    i=1
    f = 0
    while i <= num:
        if num%i == 0:
            f += 1
        i += 1
    if f == 2:
        print(num,end=' ')
    num += 1    
    


# In[19]:


# ArmStrong number :

num = int(input('Enter the number : '))
num1 = num
s = 0
a = len(str(num))
while num != 0:
    r = num%10
    s += (r**a)
    num = num//10
if s == num1:
    print('Armstrong number')
else:
    print('Not Armstrong number')


# In[15]:


#Armstrong number upto n

n = int(input('Enter the higher range number :'))

for i in range(10,n+1):
    a = len(str(i))                 #To determine the length to multiply the reminder a, n times
    b= i                            #To save the value in another variable b
    s = 0                           # Variable to store the sum
    while i!= 0:
        r = i%10
        s = s+(r**a)
        i = i//10
    if s == b:
        print(b,end=' ')


# In[2]:


w = 'harsha'
print('length of the word is :',len(w))
a = w[0]+w[1]+w[2]+w[3]+w[4]+w[5]
b = w[5]+w[4]+w[3]+w[2]+w[1]+w[0]
print('The word is                 : ', a)
print('The word in reverse order is: ', b)


# In[2]:


#To print given string in reverse order

w = input('enter a word :')
L = len(w)
R = ''
while L > 0:
    R = R+w[L-1]
    L = L-1
print('Reverse string is :',R)


# In[55]:


# Palindrome string
W = input('Enter a word :')
L = len(W)
R = ''
while L > 0:
    R = R+W[L-1]
    L = L-1
print('Reverse string is :',R)

if W == R:
    print('The string is PALINDROME string')
else:
    print('The string is NOT PALINDROME string')


# In[4]:


#To print given number in reverse order
n = int(input('Enter the number :'))
s = 0
while n > 0:
    r = n%10
    s = (s*10) + r
    n = n//10
print('The number in Reverse order is :',s)


# In[9]:


#To print given number in reverse order and to check if its palindrome number or not
n = int(input('Enter the number :'))
a = n
s = 0
while n > 0:
    r = n%10
    s = (s*10) + r
    n = n//10
print('The number in Reverse order is :',s)

if a == s:
    print('The number is PALINDROME')
else:
    print('The number is NOT PALINDROME')

