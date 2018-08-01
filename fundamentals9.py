
# coding: utf-8

# In[ ]:


#Function to find biggest number given 2 arguments
def max(num1,num2):
    '''This function is used to find the bigger number
        num1:formal int parameter 1
        num2:formal int parameter 2
        '''
    if num1 > num2:
        result = num1
    else:
        result = num2
    return result    


# In[10]:


x = int(input('Enter the first number :'))
y = int(input('Enter the second number :'))
z = max(x,y)
print('The bigger number is : ', z)


# In[5]:


#Function to find given number is Even or Odd
'''This function is  used to find the given number is
        Even or odd
        num : Formal int parameter
        '''
def isEven(num):
    if num%2 == 0:
        return True
    else:
        return False
        
    


# In[7]:


n = int(input('Enter the value : '))
if isEven(n):
    print('EVEN Number')
else:
    print('ODD Number')

