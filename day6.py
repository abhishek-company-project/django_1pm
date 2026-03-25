# what is string in python

#! string is a data type in python , if you want to store multiple character in single 
# ! variable you can use string . 
# ? it is represent by '',""
# 
#

# str="shantii";

# length of string = character count
# print(len(str))

# if i want to access every character why position (index)
# print(str[0])
# print(str[-1])
# print(str[int(len(str)/2)])


# for i in range(len(str)): 
#     print(str[i])





# str="shantii infosoft";
# vowel=0;

# get one by one all character
# check every character with "a" , "e" ,"i ","o",u
# if condition are match vowel ++

# for i in range(len(str)):
#     if str[i]=="a" or str[i]=="e" or str[i]=="o" or str[i]=="i" or str[i]=="u":
#         vowel+=1;

# print(vowel)


# str="my na me is abhi shek";
# count=0;

# for i in range(len(str)):
#     if str[i]==" ":
#         count+=1;

# print(count+1)


# str="shanti"
# newstr="";
# for i in range(len(str)):
#     # print(str[i])
#     newstr=str[i]+newstr;  # change the sequence of addition



# # for i in range(len(str)-1,-1,-1):
# #     # print(str[i])
# #     newstr=newstr+str[i]

# print(newstr)    





# str="abhishek gurjar";
# # output = AG

# # get first character of a string that is first world character
# # find the space and get next character
# world="";
# for i in range(len(str)):
#     if i==0:
#         world+=str[i];

#     if str[i]==" ":
#         world+=str[i+1]

# print(world.upper())        