# find smallest number from list
list=[90,3,57,5,56]
smallest_num=list[0]
for i in list:
    if smallest_num>i:
        smallest_num=i
print("smallest number is ",smallest_num)
