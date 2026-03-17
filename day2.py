# 🔢 What are Bitwise Operators?

# Bitwise operators work directly on the binary (bits) of numbers.

# Operator	Name	Meaning
# &	AND	1 if both bits are 1
# `	`	OR
# ^	XOR	1 if bits are different
# ~	NOT	Inverts bits
# <<	Left Shift	Shifts bits left
# >>	Right Shift	Shifts bits right
# 🧠 Example: Understanding Step by Step

# Let’s take two numbers:

# a = 5
# b = 3
# Step 1: Convert to Binary
# 5 = 0101
# 3 = 0011
# ✅ 1. Bitwise AND (&)
# print(a & b)
#   0101
# & 0011
# -------
#   0001  → 1

# 👉 Output: 1

# ✔ Only positions where both bits are 1

# ✅ 2. Bitwise OR (|)
# print(a | b)
#   0101
# | 0011
# -------
#   0111  → 7

# 👉 Output: 7

# ✔ If any bit is 1

# ✅ 3. Bitwise XOR (^)
# print(a ^ b)
#   0101
# ^ 0011
# -------
#   0110  → 6

# 👉 Output: 6

# ✔ If bits are different

# ✅ 4. Bitwise NOT (~)
# print(~a)

# 👉 Formula:

# ~a = -(a + 1)

# So:

# ~5 = -(5 + 1) = -6

# 👉 Output: -6

# ✅ 5. Left Shift (<<)
# print(a << 1)
# 0101 → 1010  (shift left by 1)

# 👉 Output: 10

# ✔ Equivalent to: a * 2

# ✅ 6. Right Shift (>>)
# print(a >> 1)
# 0101 → 0010

# 👉 Output: 2

# ✔ Equivalent to: a // 2

# 💡 Real Example (Use Case)

# Check if a number is even or odd using bitwise AND:

# num = 6

# if num & 1 == 0:
#     print("Even")
# else:
#     print("Odd")

# ✔ Explanation:

# Last bit of even numbers = 0

# Last bit of odd numbers = 1



# Comparison Operators
# Comparison operators are used to compare two values:

# Operator	 Name	                  Example	Try it
# ==	  Equal	                      x == y	
# !=	  Not equal	                    x != y	
# >	      Greater than           	     x > y	
# <	      Less than	                       x < y	
# >=	  Greater than or equal to	     x >= y	
# <=	  Less than or equal to         	x <= y

# print(6!=5)
# print(6!=6)
# print(6==6)
# print(6%2!=2)






# Logical Operators
# Logical operators are used to combine conditional statements:

# Operator	Description	                 Example	                               Try it
# and (both condition are true) 	Returns True                     if both statements are true	            x < 5 and  x < 10	
# or (any one condition are true)	Returns True                      if one of the statements is true	         x < 5 or x < 4	
# not	Reverse the result,               returns False if the result is true	      not(x < 5 and x < 10)


# x=7;
# y=2

# print(x%2==0 and y>=3)
# print(x%2==0 or y>=3)
# print(x%2==0 or not y>=3)