a=int(input("enter a number : "));
b=int(input("enter a number : "));
c=int(input("enter a number : "));
max1=max2=max3=0;
while(a):
    rem=a%10;
    a=a//10;
    if(rem>max1):
        max1=rem;
while(b):
    rem=b%10;
    b=b//10;
    if(rem>max2):
        max2=rem;
while(c):
    rem=c%10;
    c=c//10;
    if(rem>max3):
        max3=rem;
if(max1<max2):
    max1=max2;
if(max1>max3):
    print(max1);
else:
    print(max3);