#!/usr/bin/env python
# coding: utf-8

# # <center>Intermediate Python<center>

# In this notebook, we’ll be more concerned with the python syntax stuff, but along with this, I've divided the “intermediate python for data science” chapter into more. I’ll bring back new chapters with the basics of Numpy, Matplotlib, and Pandas along with practices.
# 
# 1. Data Structures 
# 2. Logic Control Flow and Filtering
# 3. Loops

# # 1. Data Structures

# Data structures are formations in which data can be kept in memory. Python offers multiple built-in data structures so that the programmer needs not to implement these from scratch. These include:
# - Dictionary
# - Tuple
# - Set
# - List (covered in the previous article: Introduction to Python for DS)

# # 1.1 Dictionary

# In[2]:


#storing data by using lists
pop = [30.55, 2.77, 39.21]
countries = ["afghanistan", "albania", "algeria"]
...
#storing data by using dictionaries, Dictionaries are supposed 
#to be more convennient to store data about data
world = {"afghanistan":30.55,"albania":2.77, "algeria":39.21}
world["albania"]


# In[3]:


world = {"afghanistan":30.55,"albania":2.77,"algeria":39.21,"albania":2.81}
world


# ### 1.1.1 Adding data in a dictionary

# In[4]:


#adding another country(key) and population(value) in the world dictionary
world["sealand"] = 0.000027
world


# In[5]:


#checking the addition of key in dictionary
"sealand" in world


# ### 1.1.2 Deleting data from a dictionary

# In[6]:


del(world["sealand"]) 
world 
#sealand (key and value) has been deleted


# ### 1.1.3 Lists vs. Dictionary

# In[ ]:





# # 1.2 Tuples

# In Python, a tuple is an ordered, immutable sequence of elements. This means that once a tuple is created, its contents cannot be modified. Tuples are similar to lists in Python, but with two key differences:
# 
# 1. Tuples are enclosed in parentheses (), whereas lists are enclosed in square brackets [].
# 2. Tuples are immutable, whereas lists are mutable.

# In[10]:


# tuple are used with "round brackets"
t = (1,2,3)


# In[11]:


# tuple indexing is just same as list indexing we covered before
t[1]


# In[12]:


# tuple slicing is just same as list slicing we covered before
t[1:]


# In[22]:


# tuples are immutable objects so no item can be changed
t[0] = '99'


# # 1.3 Sets

# In Python, a set is an unordered collection of unique elements. This means that each element in a set is unique (i.e., it can only appear once in the set), and the elements are not stored in any particular order. Sets are used when you need to store a collection of elements, but you don’t care about the order or the duplicates.

# In[26]:


set = {1,2,3}

# sets are collections of unique items
{1,2,3,1,2,1,2,3,3,3,3,2,2,2,1,1,2}


# In[27]:


# set item add
set.add(9)
set


# In[28]:


# set allow intersection, difference, union among other operations
s1 = {1,2,3}
s2 = {3,4,5}
intersection = s1.intersection(s2)
print("intersection is:", intersection)
union = s1.union(s2)
print("union is:", union)
difference = s1.difference(s2)
print("difference is:", difference)


# In[29]:


# Ashort hand for 
a={1,3,4,6,'g'}
b = {2, 3, 4, 5}

print("Intersection: ",a & b)
print("Union: ",a | b)


# # 2. Logic Control Flow and Filtering

# ### 2.1 If

# In[32]:


#basic syntax
#if condition :
#    expression


# In[33]:


z = 4
if z % 2 == 0 :
  print("checking " + str(z))
  print("z is even")


# ### 2.2 else

# In[34]:


#basic syntax
#if condition :
#  expression
#else :
#  expression  


# In[35]:


z = 5
if z % 2 == 0 : # False
   print("z is even")
else :
  print("z is odd")


# ### 2.3 elif

# In[37]:


#basic syntax
#if condition :
#   expression
# elif condition :
#   expression
# else :
#   expression


# In[38]:


z = 3
if z % 2 == 0 :
  print("z is divisible by 2") # False
elif z % 3 == 0 :
  print("z is divisible by 3") # True
else :
  print("z is neither divisible by 2 nor by 3")


# # 3. Loops

# - while
# - for

# ### 3.1 while

# In[40]:


# while condition :
#   expression


# In[41]:


error = 50.0
# 0.78125
while error > 1: # False
  error = error / 4
  print(error)


# ### 3.2 for loop

# In[43]:


#basic syntax
# for var in seq :
#   expression

# # for each var in seq, execute expression


# In[45]:


fam = [1.73, 1.68, 1.71, 1.89]
for height in fam :
  print(height)


# ### enumerate, loops over list, dictionary, NumPy arrays

# In[46]:


fam = [1.73, 1.68, 1.71, 1.89]
for index, height in enumerate(fam) :
  print("index " + str(index) + ": " + str(height))


# In[47]:


for c in "family" :
  print(c.capitalize())


# In[48]:


#looping over dictionary
world = { "afghanistan":30.55,"albania":2.77,"algeria":39.21 }
for key, value in world.items() :
  print(key + "--" + str(value))


# In[49]:


import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
bmi = np_weight / np_height ** 2
for val in bmi :
  print(val)


# # Important Note

# Important note
# I’m working on #100daysofMLCode, where I am starting with the beginner level, I’ll post the weekly content or more in a week in a form of a crux. If you’re a beginner and want to enhance your knowledge of Data science along with practice implementation, we can get connected through LinkedIn, Medium, and GitHub here.

# # LinkedIn

# Here is my LinkedIn profile in case you want to connect with me. I’ll be happy to be connected with you. <br>
# Lets Connected: https://www.linkedin.com/in/sania-mohiu-ud-din-277047193 <br>
# GitHub: https://github.com/SaniaGMD
