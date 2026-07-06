# Zargol Kanani

class Customer:

    # initialize customer information
    def __init__(self, name : str, email : str, phoneNumber : str):
        self.name = name
        self.email = email
        self.phoneNumber = phoneNumber

    """
    validate email format:
    - exactly one @
    - validate username
    - validate domain and exetension
    """
    def is_valid_email(self):   

        errors = [] # list to store all validation errors
        parts = self.email.split("@") #split email

        
        if len(parts) != 2: #check the count of @
            errors.append("Error 1: email must contain exactly one @") 
        else:
            username = parts[0]
            domain   = parts[1]
            
            # ----check username----
            # username should not be empty 
            if username=="":
                errors.append("Error 2: the username is empty")
            # check each char
            for char in username: 
                # only '_' at first of username, letters and digits are allowed
                if not (username[0] == "_" or char.isalnum()):
                    errors.append("Error 3: username isn't valid")
                    break
                

            # ----check domain----
            # domain must have one dot   
            if '.' not in domain:
                errors.append("Error 4: there isn't '.' in domain") 
            else:
                domain= domain.split(".")
                # ensure only one dot exist
                if(len(domain) != 2):
                    errors.append("Error 5: there is more than one '.'")
                else:
                    part1 = domain[0] # domain name
                    part2 = domain[1] # extension (com, org, net)

                    # domain should not be empty
                    if part1 == "":
                        errors.append("Error 6: domain part is empty")

                    # check valid extensions
                    if part2 not in ['com','org','net']:
                        errors.append("Error 7: invalid email extensions") 
        # return final result
        return len(errors)==0, errors
    
    """
    validate phone number format:
    - must not be empty
    - must contain only digit (except + or - at the start)
    - length must be >= 10
    """
    def is_valid_phone(self):

        errors = []
        # check if phone number is empty
        if self.phoneNumber == "":
            errors.append("Error 1: phone number is empty")
            return errors # prevent crash

        # check if phone number starts with valid char and rest are digit
        if not ((self.phoneNumber[0] == '+' or self.phoneNumber[0] == '-' or self.phoneNumber[0] == '0') and (self.phoneNumber[1:].isdigit())):
            errors.append("Error 2: phone number isn't valid")

        # length validation
        if (self.phoneNumber[0] == '+' or self.phoneNumber[0] == '-'):
            if not (10 <= len(self.phoneNumber[1:]) <= 15): 
                    errors.append("Error 3: invalid phone number length")
        else:
            if not (10 >= len(self.phoneNumber)): # start with 0
                    errors.append("Error 3: invalid phone number length")
        # return final result
        return len(errors)==0, errors        




# ----test-----
customer_1 = Customer('zargol','@gmailcom','0fdfsda98581') 
# print(customer_1.is_valid_phone() ) 
# print(customer_1.is_valid_email() )