n=int(input("enter a number : "));
i=1;
while(i<=n):
    if(not i%2):#not has less priority than %
       print(i);
    i+=1;