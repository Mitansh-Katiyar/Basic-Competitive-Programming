a=int(input("enter a number : "));
b=int(input("enter a number : "));
num1=a;
max=0;
while(num1):
    rem=num1%10;
    num1=num1//10;
    if(max<rem):
        max=rem;
num1=b;
max2=0;
while(num1):
    rem=num1%10;
    num1=num1//10;
    if(max2<rem):
        max2=rem;
if(max>max2):
    print(max);
else:
    print(max2);