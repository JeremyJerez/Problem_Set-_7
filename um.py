# Python_Intro
# Problem Set 7
#A series of exercises for CS50 hands-on projects
"""
This one"s my approach to the "Regular, um, Expressions" problem
"""
import re


def main():
    print(count(input("Text: ")))


def count(s):
    um = re.findall(r"\b\W*um\W*", s, re.IGNORECASE )
    return len(um)


if __name__ == "__main__":
    main()
