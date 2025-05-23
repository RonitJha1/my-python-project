#1) List: Write a Python program to add all the elements in a list [2, 4, 6, 8].
# a=[2,3,6,8]
# print(a)
#2) Tuple: Create a tuple with five elements and print its length.
# a=(1,2,3,4,5)
# print(len(a))
# a=input("enter numbers or letter ")
# print (len(tuple(a)))
# 3) Dictionary: Create a dictionary with three key-value pairs representing a person's name, age,and city. Print the value for the "age"
# key.
# a={
#     "name":"Ronit jha",
#     "age":17,
#     "city":"brt"
# }
# print(a["age"])
from itertools import count

#4) List: Write a program that takes 5 numbers as input from the user and stores them in a list.
# a=(input("enter number"))
# print (list(a))

#5) Dictionary: Write a program to add a new key-value pair 'country': 'Nepal' to an existing dictionary.
# a={
#     "name":"Ronit jha",
#     "class":10,
#     "age":17,
#     "city":"biratnagar"
# }
# a["country"]="Nepal"
# print(a)



# 🔹 Intermediate Level (Q6–Q15)
#1) List: Remove all duplicate items from the list [1, 2, 2, 3, 4, 4, 5].
# a=[1,2,2,3,4,4,5]
# a.remove(4)
# print(a)
# a.remove(2)

#2) Tuple: Convert the list [1, 2, 3, 4] into a tuple.
# a=[1,2,3,4]
# print(tuple(a))

# 3)Dictionary: Write a Python program to count the number of times each element appears in the list ['apple', 'banana', 'apple', 'orange',
# 'banana', 'apple'] using a dictionary.
# a=["apple","banana","apple","orange","banana","apple"]
# b={}
# for a in a:
#     if a in b:
#         b[a]+=1
#     else:
#         b[a]=1
# print(b)




# 4)List & Dictionary: Create a list of student names and a dictionary to store their marks. Assign random marks and display each student's
# name with their mark.
# a=["Ronit","Rupesh","sailesh","navyata"]
# a={
#     "Ronit":50,
#     "Rupesh":51,
#     "sailesh":69,
#     "navyata":60
# }
# print(a)

# 5)Tuple: Write a program to find the maximum and minimum elements in a tuple (9, 3, 5, 1, 7).
# a=(9,3,5,1,7)
# b=max(a)
# c=min(a)
# print("maximum no is",b)
# print("minimum no is",c)
# 6)List: Reverse a list without using the built-in reverse function.
# a=[9,8,7,6,5,4,3,2,1]
# a.sort()
# print(a)

# 7)Dictionary: Write a program to merge two dictionaries:
# d1 = {'a': 100, 'b': 200}
# d2 = {'c': 300, 'd': 400}

# a = {'a': 100, 'b': 200}
# b = {'c': 300, 'd': 400}
# a.update(b)
# print(a)

# 8)List: Given a list of integers, write a program to separate even and odd numbers into two new lists.
# a=[1,2,3,4,5,6,7,8,9,10]
# even=[]
# odd=[]
# for i in a:
#     if i %2==0:
#         even.append(i)
#     else:
#         odd.append(i)
#
# print("even no is",even)
# print("odd no is",odd)
# 9)Tuple: Write a program to check if a particular value exists in a tuple.
a=input("name that exist")
# print("ronit"in a)
# print("jha"in a)
# print("god" in a)
# print("good"in a)
# print("boy"in a)
# if "ronit" in a:
#     print("yes this value exist")
# elif"jha" in a:
#   print("yes this value exist")
# else:
# elif"good" in a:
#  print("yes this value exist")
# elif"boy" in a:
#  print("yes this value exist")
#                print("this value doesn't exist")


# 10)List-Tuple-Dictionary: Given a list of tuples like [('a', 1), ('b', 2), ('c', 3)], convert it into a dictionary.
# a=[("a",1),("b",2),("c",3)]
# print(dict(a))
