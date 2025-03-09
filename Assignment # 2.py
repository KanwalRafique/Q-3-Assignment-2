# PYTHON OPERATORS

# --------------- ARITHMETIC OPERATORS ---------------

print("---------Examples of ARITHMETIC OPERATORS---------")

a = 10
b = 3

# Addition
print("Addition:", a + b)  # 10 + 3 = 13

# Subtraction
print("Subtraction:", a - b)  # 10 - 3 = 7

# Multiplication
print("Multiplication:", a * b)  # 10 * 3 = 30

# Division (returns float)
print("Division:", a / b)  # 10 / 3 = 3.3333

# Floor Division (returns integer)
print("Floor Division:", a // b)  # 10 // 3 = 3

# Modulus (remainder)
print("Modulus:", a % b)  # 10 % 3 = 1

# Exponentiation (power)
print("Exponentiation:", a ** b)  # 10^3 = 1000


#-----------------------------------------------------------------------

# --------------- ASSIGNMENT OPERATORS ---------------
print("---------Examples of ASSIGNMENT OPERATORS---------")

# Assigning values
x = 10
print("Initial value of x:", x)  # x = 10

# Addition assignment
x += 5  # Equivalent to x = x + 5
print("After x += 5:", x)  # 10 + 5 = 15

# Subtraction assignment
x -= 3  # Equivalent to x = x - 3
print("After x -= 3:", x)  # 15 - 3 = 12

# Multiplication assignment
x *= 2  # Equivalent to x = x * 2
print("After x *= 2:", x)  # 12 * 2 = 24

# Division assignment
x /= 4  # Equivalent to x = x / 4
print("After x /= 4:", x)  # 24 / 4 = 6.0

# Floor division assignment
x //= 2  # Equivalent to x = x // 2
print("After x //= 2:", x)  # 6.0 // 2 = 3.0

# Modulus assignment
x %= 2  # Equivalent to x = x % 2
print("After x %= 2:", x)  # 3 % 2 = 1.0

# Exponentiation assignment
x **= 3  # Equivalent to x = x ** 3
print("After x **= 3:", x)  # 1.0 ** 3 = 1.0

# Bitwise AND assignment
x = 5  # Reset x
x &= 3  # Equivalent to x = x & 3
print("After x &= 3:", x)  # 5 & 3 = 1 (bitwise AND)

# Bitwise OR assignment
x |= 2  # Equivalent to x = x | 2
print("After x |= 2:", x)  # 1 | 2 = 3 (bitwise OR)

# Bitwise XOR assignment
x ^= 3  # Equivalent to x = x ^ 3
print("After x ^= 3:", x)  # 3 ^ 3 = 0 (bitwise XOR)

# Bitwise left shift assignment
x = 2  # Reset x
x <<= 2  # Equivalent to x = x << 2
print("After x <<= 2:", x)  # 2 << 2 = 8

# Bitwise right shift assignment
x >>= 1  # Equivalent to x = x >> 1
print("After x >>= 1:", x)  # 8 >> 1 = 4

#----------------------------------------------------------

# --------------- COMPARISON OPERATORS ---------------
print("---------Examples of COMPARISON OPERATORS----------")

a = 10
b = 5

# Equal to
print("a == b:", a == b)  # False (10 is not equal to 5)

# Not equal to
print("a != b:", a != b)  # True (10 is not equal to 5)

# Greater than
print("a > b:", a > b)  # True (10 is greater than 5)

# Less than
print("a < b:", a < b)  # False (10 is not less than 5)

# Greater than or equal to
print("a >= b:", a >= b)  # True (10 is greater than or equal to 5)

# Less than or equal to
print("a <= b:", a <= b)  # False (10 is not less than or equal to 5)

#-------------------------------------------------------------------

# --------------- LOGICAL OPERATORS ---------------
print("----------Examples of LOGICAL OPERATORS------------")

x = True
y = False

# Logical AND
print("x and y:", x and y)  # False (True AND False = False)

# Logical OR
print("x or y:", x or y)  # True (True OR False = True)

# Logical NOT
print("not x:", not x)  # False (NOT True = False)
print("not y:", not y)  # True (NOT False = True)

# Using logical operators with numbers
a = 10
b = 0

print("(a > 5) and (b == 0):", (a > 5) and (b == 0))  # True AND True = True
print("(a < 5) or (b == 0):", (a < 5) or (b == 0))  # False OR True = True
print("not (a == 10):", not (a == 10))  # NOT True = False


#--------------------------------------------------------------------

# --------------- IDENTITY OPERATORS ---------------
print("------------Examples of IDENTITY OPERATORS------------")

a = 10
b = 10
c = [1, 2, 3]
d = [1, 2, 3]

# 'is' operator (checks if two variables refer to the same object)
print("a is b:", a is b)  # True (same memory location for integers)

print("c is d:", c is d)  # False (different memory locations for lists)

# 'is not' operator (checks if two variables do not refer to the same object)
print("a is not b:", a is not b)  # False (same memory location)

print("c is not d:", c is not d)  # True (different memory locations)

# Additional Example: Mutable vs Immutable
x = "hello"
y = "hello"
print("x is y:", x is y)  # True (Python optimizes and points to the same string object)

p = [1, 2, 3]
q = p  # Assigning same reference
print("p is q:", p is q)  # True (q refers to the same list as p)

r = p[:]  # Creates a new list with the same content
print("p is r:", p is r)  # False (r is a new list)

#-----------------------------------------------------------------

# --------------- MEMBERSHIP OPERATORS ---------------
print("----------Examples of MEMBERSHIP OPERATORS-----------")

# Using 'in' operator
numbers = [1, 2, 3, 4, 5]
print("3 in numbers:", 3 in numbers)  # True (3 is present in the list)

print("10 in numbers:", 10 in numbers)  # False (10 is not in the list)

# Using 'not in' operator
print("10 not in numbers:", 10 not in numbers)  # True (10 is not present)

# Membership in strings
text = "Hello, Python!"
print("'Python' in text:", "Python" in text)  # True ("Python" exists in the string)

print("'Java' not in text:", "Java" not in text)  # True ("Java" is not in the string)

# Membership in tuples
tuple_data = ('apple', 'banana', 'cherry')
print("'banana' in tuple_data:", 'banana' in tuple_data)  # True

# Membership in dictionaries (checks keys, not values)
student_scores = {"Alice": 90, "Bob": 85, "Charlie": 92}
print("'Alice' in student_scores:", "Alice" in student_scores)  # True (checks keys)

print("'David' not in student_scores:", "David" not in student_scores)  # True (David is not a key)

#------------------------------------------------------------------

# --------------- BITWISE OPERATORS ---------------
print("Examples of BITWISE OPERATORS")

a = 5  # 0101 in binary
b = 3  # 0011 in binary

# Bitwise AND (&)
print("a & b:", a & b)  # 0101 & 0011 = 0001 (1 in decimal)

# Bitwise OR (|)
print("a | b:", a | b)  # 0101 | 0011 = 0111 (7 in decimal)

# Bitwise XOR (^)
print("a ^ b:", a ^ b)  # 0101 ^ 0011 = 0110 (6 in decimal)

# Bitwise NOT (~)
print("~a:", ~a)  # ~0101 = -(0101 + 1) = -6 (Two's complement)

# Left Shift (<<)
print("a << 1:", a << 1)  # 0101 << 1 = 1010 (10 in decimal)

# Right Shift (>>)
print("a >> 1:", a >> 1)  # 0101 >> 1 = 0010 (2 in decimal)





