# Zargol Kanani

# BMI
# get informations from user
first_name = input("What's your name? ")
age = int(input("How old are you? "))
height = float(input("How tall are you?(m) "))
weight = int(input("How much do you weight? "))

calculate_BMI = weight / (height**2)

print(f"Mr./Ms. {first_name}, {age} years old, height {height}m, weight {weight}kg, your body mass index is {calculate_BMI:.2F}")