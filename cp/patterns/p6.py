n=int(input("enter a number : "));
for i in range(n):
    for j in range(n+2):
        if(j<n+2-i):
            if(j==0 or j==n+1-i):
                print("*",end="");
            else:
                print("_",end="");
    print("");