# 1)question
# *
# **
# ***
# ****
# for i in range(1,5):
#     print("*"*i)
# 2)question
# *
# **
# ***
# ****
# *****
# i=1
# while i<=5:
#     print("*"*i)
#     i+=1
# 3)question
# 12345
# 12345
# 12345
# 12345
# for i in range(1,5):
#     for e in range(1,6):
#         print(e,end="")
#     print()

# 4)question
# 11111
# 22222
# 33333
# 44444
# 55555
# i=1
# while i<=5:
#     for e in range(1,6):
#         print(i,end="")
#     print()
#     i+=1
# 5)question
# 12345
# 23456
# 34567
# 45678
# 56789
# a=0
# for i in range(1,6):
#     print()
#     for e in range(1,6):
#         print(e+a,end="")
#     a+=1

# 6)question
# *
# ** *
# ** ** *
# ** ** ** *
# ** ** ** ** *
# ** ** ** ** ** *
# b=6
# for i in range(1,b+1):
#     print(' '*(b-i),end=" ")
#     print("*"*(2*i-1))

# 7)question
# a =int(input("enter a no and it make the dimond sape :"))
# for i in range(1, a + 1):
#     print(' ' * (a - i) + '*' * (2 * i - 1))
# for i in range(a - 1, 0, -1):
#     print(' ' * (a - i) + '*' * (2 * i - 1))