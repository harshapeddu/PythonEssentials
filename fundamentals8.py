
# coding: utf-8

# In[2]:


#to display numbers from -n to n

n = int(input('Enter the number : '))
for i in range(-n,n+1):
    print(i,end=" ")
    


# In[4]:


#To demostrate the break function.
i = 1
while i <= 10:
    if i == 5:
        break
    print(i,end=' ')
    i = i+1
    


# In[5]:


# To demonstrate the break function

for i in range(1,11):
    if i == 5:
        break
    print(i,end=' ')


# In[7]:


# To demonstrate the continue function

for i in range(1,11):
    if i == 5:
        continue
    print(i,end=' ')

