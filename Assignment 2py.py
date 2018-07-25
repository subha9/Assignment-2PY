
# coding: utf-8

# In[11]:


#Write a program which accepts a sequence of comma-separated numbers from console and
#generate a list.
values =input("please enter coma seperates numbers")
list = values.split(",")
print ("list : ", list)


# In[12]:


#Create the below pattern using nested for loop in Python.


n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')


# In[13]:


#Write a Python program to reverse a word after accepting the input from the user.

PS = input(" Please enter word ")
for char in range(len(PS) - 1, -1, -1):
    print(PS[char], end="")
print("\n")


# In[14]:


#4. Write a Python Program to print the given string in the format specified in the sample
#output.
#WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN,
#SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens

print("WE, THE PEOPLE OF INDIA,\n\thaving solemnly resolved to constitute India into a SOVEREIGN, ! \n\t\tSOCIALIST, SECULAR, DEMOCRATIC REPUBLIC \n\t\tand to secure to all its citizens ")

