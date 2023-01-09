# print("Half Pyramid of Stars(*)")
# n=int(input("Enter a number:"))
# for i in range(n):
#     for j in range(i+1):
#         print("* ",end="")
#     print()


num=int(input("Enter a number:"))
k=1
for i in range(1,num+1):
    for j in range(1,k+1):
        print(k,end=" ")
    k=k+2
    print()