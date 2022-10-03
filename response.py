# Python_Intro
# Problem Set 7
#A series of exercises for CS50 hands-on projects
"""
This one"s my approach to the "Watch on YouTube" problem
"""
from validator_collection import validators

def main():
    Email = input("what's your email address? ")
    try:
        Emailvalidation = validators.email(Email)
        print("Valid")
    except:
        print("Invalid")

if __name__ == "__main__":
    main()
