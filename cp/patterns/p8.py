n= int(input("enter a number : "));
status=1;
for i in range(n):
    status=1;
    for j in range(2*n-1):
        if(j>=i and j<=2*n-1-i):
            if(status):
                print("*",end="");
            else:
                print(" ",end="");
            status=1-status
        else:
            if(j<i):
                print("_",end="");
            else:
                print(" ",end="");
    print();