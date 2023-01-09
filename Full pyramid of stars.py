# print("Full Pyramid of Stars(*)")
# n=int(input("Enter a number:"))
# for i in range(0,n):
#     for s in range(0,n-i-1):
#         print(" ",end="")
#     for j in range(0,i+1):
#         print("* ",end="")
#     print()



rows=int(input("enter the number:"))
for i in range(rows):
    print(' ' * (rows-i -1) + str(i) * (2*i+1))