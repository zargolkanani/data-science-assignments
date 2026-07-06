# Zargol Kanani

# get numbers and value
first = int(input("Enter first value: "))
second = int(input("Enter second value: "))
third = int(input("Enter third value: "))
fourth = int(input("Enter fourth value: "))
value = int(input("Enter a value: "))

# make a list
numbers=[first,second,third,fourth]

count = 0
for num in numbers:
    if value == num:
        count+=1

print(f"There are {count} {value} in the list")
