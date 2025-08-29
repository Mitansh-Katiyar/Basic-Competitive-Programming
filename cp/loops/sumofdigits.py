n=int(input("enter a number : "));
sum=0;
rem=0;
while(n):
    rem=n%10;
    n=n//10;
    sum+=rem;
print(sum);