n=int(input("enter a number : "));
for i in range(1,n+1):
    for j in range(1,n+1):
        if(j<=i):
            if(j%2):
                print(j,end="")
            else:
                print("*",end="");
    print();