n=int(input("enter a number : "));
for i in range(2*n):
    for j in range(2*n):
        if(i<n):
            if(j>n-i-1 and j<n+i):
                print(" ",end="");
            else:
                print("*",end="");
        if(i>n-1):
            if(j>i-n and j<2*n-1-(i-n)):
                print(" ",end="");
            else:
                print("*",end="");
    print();