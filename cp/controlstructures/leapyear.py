year=int(input("Enter a year : "));
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("LEAP YEAR");
        else:
            print("Non Leap Year");
    else:
        print("Leap Year");
else:
    print("Non Leap Year");
