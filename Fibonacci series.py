# program to find fibonacci series using loops
# num=int(input("Enter number="))
# n1,n2=0,1
# sum=0
# if num<=0:
#     print("Please enter n umber greater than 0")
# else:
#     for i in range(0,num):
#         print(sum ,end=" ")
#         n1=n2
#         n2=sum
#         sum=n1+n2


i=1
n=int(input("Enter how many numbers to be printed>\n"))
n1,n2=0,1
while i<=n:
    print(n1)
    n1,n2=n2,n1+n2
    i+=1
