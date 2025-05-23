# 🔸 Mixed Python Data Structure & Loop Questions

#1) List + Loop: Write a Python program to iterate over a list of numbers and print only the even numbers.
# a=[1,2,3,4,5,6,7,8,9,10]
# for i in a:
#     if i %2==0:
#         print(i)
# 2)Tuple + Dictionary + Loop: Given a tuple of student names and a dictionary with their marks, print each student’s name and mark using a
# loop.



# 3)Dictionary + Loop: Create a dictionary of items and their prices. Use a loop to print only those items with price > 100.
# a={
#     "pen":50,
#     "copy":150,
#     "ps5":1000,
#     "mind":10,
#     "sailesh":100
# }
# for i in a:
#     if a[i]>=100:
#         print(i)




# 4)List + Dictionary + Loop: From a list of strings, create a dictionary with each word as the key and its length as the value using a loop.
# Example: ["apple", "banana", "kiwi"] → {'apple': 5, 'banana': 6, 'kiwi': 4}

# 5)Tuple + List + Loop: Convert a tuple of numbers into a list, then use a loop to create a new list that contains only numbers greater
# than 50.
# c=(100,120,50,65,10,20,6,84,39,75,29,48,24,94,74,)
# i=list(c)
# for a in i:
#     if a>=50:
#         print(a)

# 6)Loop + Dictionary: Write a program that takes 5 user inputs (names) and stores them as keys in a dictionary with the length of each name
# as the value.
# a=input("Enter first person name:")
# b=input("Enter second person name:")
# c=input("Enter third person name:")
# d=input("Enter fourth person name:")
# e=input("Enter fifth  person name:")
# f={a,b,c,d,e}
#

# 7)List + Tuple + Dictionary + Loop: Given a list of tuples representing student names and grades, store them in a dictionary and print
# all students who scored above 80.
# c=[("ronit",90),("sailu",70),("rupa",91)]
# i=dict(c)
# for b, a in i.items():
#     if a>=80:
#         print(b)

# 8)Loop + Nested Dictionary: Write a program that asks the user to input data for 3 students (name, age, grade), then stores it in a nested
dictionary and prints it neatly.
print("enter first student information")
a=input("enter your name ")
b=input("entera your age")
c=input("grade of  student")
print("enter second student information")
e=input("enter your name ")
f=input("entera your age")
g=input("grade of  student")
print("now enter third student details")
i=input("enter your name ")
j=input("entera your age")
k=input("grade of  student")
info={
    "student1":{
        "name":a,
        "age":b,
        "grade":c
    },
    "student2":{
        "name": e,
        "age": f,
        "grade": g
    },
    "student3":{
        "name": i,
        "age": j,
        "grade": k
    }
}
print(info["student1"])
print(info["student2"])
print(info["student3"])
# 9)List + Dictionary + Loop: Given a list of fruits, count how many times each fruit appears using a loop and store the result in a
# dictionary.
# a=["apple", "banana", "apple", "orange", "banana"]
# b={}
# for a in a:
#     if a in b:
#         b[a]+=1
#     else:
#         b[a]=1
# print(b)

# 10)All-In-One: Write a program that:
# Starts with a tuple of subjects
# Takes marks for each subject from the user
# Stores them in a dictionary
# Adds all marks using a loop
# Then stores the result in a list as [total, average] and prints it.

# subjects = ("Math", "Science", "English", "Computer", "Nepali")
# marks = {}
# for subject in subjects:
#     mark = int(input(f"Enter marks for {subject}: "))
#     marks[subject] = mark
# total = 0
# for mark in marks.values():
#     total += mark
# average = total / len(subjects)
# result = [total, average]
# print("\nResult (Total, Average):", result)
# more need to practice