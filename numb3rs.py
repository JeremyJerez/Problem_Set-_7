# Python_Intro
# Problem Set 7
#A series of exercises for CS50 hands-on projects
"""
This one"s my approach to the "NUMB3RS" problem
"""
import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if  re.search("^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        number =ip.split(".")
        for x in number:
            if int(x) < 0 or int(x) > 255:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()
