
# coding: utf-8

# In[28]:


# Program to display simple n * n matrix)
n = int(input('Enter the matrix size : '))
for i in range(1, n+1):
    for j in range(1,n+1):
        print('X',end=' ')
    print()


# In[27]:


# Program to display simple multiplication matrix:
n = int(input('Enter variable for matrix : '))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i*j,end='   ')
    print()
    print()
    


# In[26]:


n = int(input('Enter the number : '))
i = 1
while i <= n:
    for j in range(1,i+1):
        print('X',end=' ')
    print()
    i = i + 1
    

