# Python_Intro
# Problem Set 7
#A series of exercises for CS50 hands-on projects
"""
This one"s my approach to the "Watch on YouTube" problem
"""
import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    if re.search(r"<iframe(.)*><\/iframe>", s):
        url = re.search(r"(http(s)?:\/\/(www\.)*youtube\.com\/embed\/)([a-z_A-Z_0-9]+)", s)
        if url:
            split = url.groups()
            return "https://youtu.be/" + split[3]

if __name__ == "__main__":
    main()
