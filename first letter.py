for i in range(7):#row
    for j in range(5):#column
        if ((j==0 or j==4) and i!=0) or ((i==0 or i==3) and(j>0 and j<4)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


