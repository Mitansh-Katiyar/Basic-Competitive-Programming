n=int(input("enter a number : "));
for i in range(2*n-1):
    for j in range(n):
        if(i<n-1):
            if(j<=i):
                print("*",end="");
        if(i==n-1):
            print("*",end="");
        if(i>n-1):
            if(j<2*n-i-1):
                print("*",end="");
    print();
