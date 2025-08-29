a=int(input("enter an angle : "));
b=int(input("enter an angle : "));
c=int(input("enter an angle : "));
if((a<90)&(b<90)&(c<90)):
    print("Acute Triangle");
elif((a==90)|(b==90)|(c==90)):
    print("Right Triangle");
else:
    print("Obtuse Triangle");