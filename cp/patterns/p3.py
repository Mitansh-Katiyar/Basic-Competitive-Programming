n=int(input("enter a number : "));
for i in range(n):
    for j in range(n):
        if(j<=n-i-1):
            print("*",end="");
    print();