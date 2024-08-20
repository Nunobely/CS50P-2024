#Vanity Plates problem from CS50P Week 2 problem set
#Problem set description is as follows:
# In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car,
#  with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

#     “All vanity plates must start with at least two letters.”
#     “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
#     “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable vanity plate;
#           AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
#     “No periods, spaces, or punctuation marks are allowed.”


def main():
    plate = input("Plate: ")
    if character_count(plate) and two_letters(plate) and numbers_middle(plate) and symbols(plate) and no_leading_zero(plate):
        print("Valid")
    else:
        print("Invalid")


def character_count(s):    #checks if character count is max 6 or minimum 2
    if len(s) <= 6 and len(s) >=2:
        return True

def two_letters(s):              #checks if plates start with digits (they shouldn't)
    return not s[0:2].isdigit()

def numbers_middle(s): # invalid if numbers in middle of plate, so check
    return not s[-1].isalpha()

def symbols(s):       # checks for special symbols and spaces
    for forbiddensymbol in "!?., ":
        if forbiddensymbol in s:
            return False
    return True

def no_leading_zero(s):                  #checks for leading zero (first number can't be zero)
    for potentialzero in s:
        if potentialzero.isdigit():
            return potentialzero != "0"
    return True

main()