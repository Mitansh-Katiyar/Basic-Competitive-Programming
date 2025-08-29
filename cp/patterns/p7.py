n=int(input("enter a number : "));
status=1;
for i in range(n):
    status=1;
    for j in range(2*n-1):
        if(j>=n-i-1 and j<=n+i-1):
            if(status):
                print("*",end="");
            else:
                print(" ",end="");
            status=1-status;
        else:
            if(j<=n-i-1):
                print("_",end="");
            else:
                print(" ",end="");
    print();