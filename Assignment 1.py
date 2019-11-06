#!/usr/bin/env python
# coding: utf-8

# In[22]:


#TASK#1

Line1 = "Twinkle, twinkle, little star,"
Line2 = "How I wonder what you are!"
Line3 = "Up above the world so high,"
Line4 = "like a diamond in the sky."
Line5 = "Twinkle, twinkle, little star,"
Line6 = "How I wonder what you are"
print(Line1)
print(Line2)
print(Line3)
print(Line4)
print(Line5)
print(Line6)


# In[7]:


#TASK#2

import sys
print("Python Version")
print(sys.version)


# In[36]:


#TASK#3

import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))


# In[ ]:





# In[1]:


#TASK#4


PI = 3.142
r = float(input("Enter the radius of the circle :"))
area = PI * r * r
print("Area of the circle is : %.2f" %area)


# In[40]:


#TASK#5


FirstName = input("Enter your first name: ")
LastName = input("Enter your last name: ")
Result = LastName + " " + FirstName
print (Result)


# In[39]:


#TASK#6


Num1= int(input("Enter your first num: "))
Num2= int(input("Enter your last num: "))
Result = Num1 + Num2
print (Result)


# In[ ]:




