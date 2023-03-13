arr=[]
lmt=int(input("Enter the array limit: "))

typ=int(input("Enter your choice 1.integer 2. string: "))
for i in range(lmt):
    if typ==1:
        inp=int(input("Enter integer values: "))
        arr.append(inp)
        print(arr)
    elif typ==2:
        inp1=input("Enter the string: ")
        arr.append(inp1)
        print(arr)
    else:
        print("There is not a third option!")