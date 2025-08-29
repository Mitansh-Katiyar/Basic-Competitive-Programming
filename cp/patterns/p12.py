n=int(input("enter a number : "));
k=1;
for i in range(n):
    k=1
    for j in range(i+1):
        print(k,end=" ");
        k+=1;
    print();