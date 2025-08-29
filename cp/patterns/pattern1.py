# #   1     #
# for i in range(1,6):
#     for j in range (1,6):
#         if(j<=i):
#             if(j%2):
#                 print(j,end="");
#             else:
#                 print("*",end="");
#     print("");
# print("");
# i=0;
# j=0;
# #   2    #

# for i in range(0,5):
#     for j in range(0,5):
#         if(j==0 or j==4):
#             print("*",end="");
#         else:   
#             print("_",end="");
#     print("");
# print("");

# #    3     #

# for i in range(0,5):
#     for j in range (0,7):
#         if(j<=6-i):
#             if(j==0 or j==6-i):
#                 print("*",end="");
#             else:
#                 print("_",end="");
#     print("");

# #sir solution 
# n=int(input("enter a number : "));
# for i in range(1,n+1):
#     print("*",end="");
#     for j in range(n+1-i):
#         print("_",end="");
#     print("*");
# print("");

# #    4    #
# n=int(input("enter a number : "));
# for i in range (0,n):
#     for j in range(1,n+1):
#         if(j<=i):
#             print("-",end="");
#         else:
#             print("*",end="");
#     print("");
# print();
#   5   #
n=int(input("enter a number : "));

for i in range(0,n):
    for j in range(0,2*n):
        if(j>n-1-i and j<n+i):
            print(" ",end="");
        else:
            print("*",end="");
    print("");

#sir solution  #
# n=int(input(("enter a number : ")));
# for i in range(1,n+1):
#    for j in range (n-i+1):
#        print("*",end="");
#    for j in range(2*i-2):
#        print(" ",end="");
#    for j in range(n-i+1):
#        print("*",end="");
#    print("");

#    6    #

for i in range (5):
    for j in range(10):
        if(j>i and j<9-i):
            print(" ",end="");
        else:
            print("*",end="");
    print("");

# sir solution #
#star = i;
#space 2n-2i;
#star=i;
# n=int(input("enter a number :  "));
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end="");
#     for j in range(2*n-2*i):
#         print(" ",end="");
#     for j in range(i):
#         print("*",end="");
# print();

#   7   #
n=int(input("enter a number : "));
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="");
    print();