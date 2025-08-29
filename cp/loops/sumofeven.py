#A inclusive or not ?
A=int(input("enter a number : "));
i=0;
sum=0;
while(i<=A):
    if(not i%2):
        sum+=i;
    i+=1;
print(sum);