#!/usr/bin/env python
# coding: utf-8

# In[2]:


def add(x, y):
    return x + y


# In[3]:


def subtract(x, y):
    return x - y


# In[4]:


def multiply(x, y):
    return x * y


# In[5]:


def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y


# In[8]:


print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")


# In[9]:


while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        break
    else:
        print("Invalid input")


# In[ ]:




