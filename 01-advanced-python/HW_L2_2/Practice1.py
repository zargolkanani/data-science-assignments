# Zargol Kanani


# get input string
string = input()

# remove spaces
string = string.strip()

# split string into words
list_of_string = string.split()

# convert all words to lowercases
lower_list = list(map(str.lower, list_of_string))

word_count = dict() # dicitionary to store word count

for word in lower_list :
    # count occurrences of each word
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1 

print(word_count)