n=int(input("enter a number : "));
copynum=n;
revnum=rem=0;
while(n):
    rem=n%10;
    n=n//10;
    revnum=revnum*10+rem;
if(copynum==revnum):
    print("YES");
else:
    print("NO");