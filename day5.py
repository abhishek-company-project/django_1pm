

# for i in range(4):
#     for j in range(4):
#        if i==0 or i==3 or j==0 or j==3:
#             print("* ",end="")
#        else:
#            print("  ",end="")    
#     print()    


# for i in range(6):
#     for j in range(1+i):
#         if i==0 or j==0 or i==5 or i==j :
#             print("* ",end="")
#         else:
#             print("  ",end="")    
#     print() 
# 
# 
# 

for i in range(5)   :
    for j in range(4-i):
        print("  ",end="")

    for k in range(1+i):
        print("* ",end="")

    print()    