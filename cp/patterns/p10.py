n=int(input("enter a number : "));
for i in range(n):
    for j in range(2*n):
        if(j>i and j<2*n-1-i):
            print(" ",end="");
        else:
            print("*",end="");
    print();
