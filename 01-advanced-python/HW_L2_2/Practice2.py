# Zargol Kanani

def age_filter(value,*args):
    
    ages = filter(lambda age: age > value, args) # remove ages smaller than value

    # categorize each age
    def categorize(age):
        if age < 40:
            return "Young"
        elif age < 65:
            return "Middle-aged"
        else:
            return "Old"
        

    return (list(map(categorize,ages)))


print(age_filter(5,4,18,30,65,50,25,36))


