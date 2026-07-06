# Zargol Kanani


# insert a string
string = input()

# remove spaces
string = string.strip()

# remove , and .
new_string = string.replace(",","").replace(".","")
print(new_string)

# make a list by the string
list_string = new_string.split(" ")

# sort by alphabet
lower_list = list(map(str.lower, list_string))
sorted_list = sorted(lower_list)
print(sorted_list)

# make a str by sorted list
sentence = " ".join(sorted_list)
print(sentence)

# reverse the second half of a sentence
second_half = sentence[len(sentence)//2:-1] 
reverse_sentence = second_half[::-1]
print(reverse_sentence)

