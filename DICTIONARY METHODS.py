# # DICTIONARY METHODS
# • keys(): Returns a view object that displays a list of all the keys in the dictionary.
# • values(): Returns a view object that displays a list of all the values in the dictionary.
# • items(): Returns a view object that displays a list of key-value tuple pairs.
# • update(): Updates the dictionary with elements from another dictionary or from an iterable  of key-value pairs.

a={
    "name":"ronit jha",
    "class":"10",
    "age":"17"
}
# keys()
b=a.keys()
print(b)
# values()
b=a.values()
print(b)
# items()
b=a.items()
print(b)
# update()
a.update({"email":"ashgreninja14@gmail.com"})
print(a)
