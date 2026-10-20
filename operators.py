# arithmetic operators
a = 4
b = 2

print(a + b)
print(a - b)
print(a * b)
print(a / b) #answer is integer but stils comes in a float function
print(a % b) #remainder
print(a ** b) #a^b

#relational/comparison operators - answer is a boolean value
a = 50
b = 20

print(a == b)
print(a != b)
print(a >= b)
print(a > b)
print(a <= b)
print(a < b)


# assignment operators
num = 10
num = num + 10  # num += 10
num -= 10
num *= 5
num /= 2
num %= 7
num **= 2

print ("num:",num)


#logical operators {not, and, or}
# 'not' single operand ke upar kaam karta hai lekin 'and','or' 2 values ke upaar kaam karta

a = 50
b = 30
print(not False)
print(not True)
print(not(a > b))


val1 = True
val2 = True
print("AND operator:", val1 and val2)
print("OR operator:", (a == b) or (a > b))


val1 = True
val2 = False
print("AND operator:", val1 and val2)
print("OR operator:", val1 or val2)

val1 = False
val2 = False
print("AND operator:", val1 and val2)
print("OR operator:", val1 or val2)




