
# names=["abhishek","aman","jay","ram"]

# arr=[[12,32,12],[43,12,3]]

# print(arr[0][0])

# print("rama" in names)

# num=[12,2,3,23,43,24,54];

# mix=["aman",234,243,True , False ,"jay"]

# max=num[0]

# for i in range(len(num)):
#     if num[i]>max:
#         max=num[i]

# print(max)

# length 4
# print(len(names))
# print(names[0][0])

# print(names[1])
# for i in range(len(names)):
#     print(names[i][-1])



# names=["abhishek","aman","jay","ram"]
# names[2]="raman"
# print(names)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)

thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)

# for i in range(len(thislist)):
#     print(thislist[i])

# for i in thislist:
#     print(i)    

# i=0;

# while i< len(thislist):
#     print(thislist[i]);
#     i+=1;



list=[12,4,2,13,5,53,15,62]
newlist=[];

# for i in list:
#     if i%2==0:
#         newlist.append(i)

# print(newlist)

# newlist = [expression for item in iterable if condition == True]

newlist=[i for i in list if i%2==0]

# newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)
