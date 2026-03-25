

# str="     abhishek  "

# slice method
# slice(starting:end-notincluded:step)

# print(str[2:6])
# print(str[:5]) # starting point is 0
# print(str[2:]) # ending point is lastindex
# print(str[:]) # starting is 0 and ending point is lastindex

# print(str[-3:-1])

# print(str)
# print(str.strip())
# print(str.replace("h","0"))

# newstr="my name-abhishek"
# print(newstr.split("-"))

# a = "Hello"
# b = "World"
# c = a + b
# print(c)

# a=10;
# b=4;

# name="shanti infosoft"

# # print("sum of two number is " , a+b)
# # print(f"sum({a}+{b}) of \'two \ooo number\' is \n {a+b}")

# # print(name.center(15,"X"))
# # print(name.count("i"))
# # print(name.encode())
# # print(name.endswith("soft"))
# print(name.find("n"))


# Write a program to compress a string by counting consecutive characters.
#  Example:
#  Input: aaabbca
#  Output: a3b2c1a1

# str="aaabbcaaa";
# count=1;
# result=""
# for i in range(1,len(str)):
#     if str[i]==str[i-1]:
#         count+=1;
#     else:
#         result+=f"{str[i-1]}{count}"
#         count=1;

#     if i==len(str)-1:
#         result+=f"{str[i]}{count}"

# print(result)