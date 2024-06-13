import re

# Task 1: Name Verification

names = ["Abraham Lincoln", "Andrew P Garfield", "peter pan", "Connor Milliken", "Jordan Alexander Williams", "Madonna", "programming is cool"]


def check_names(names):
    # Regex pattern for a valid name (alphabetic characters and spaces)
    pattern = r'^[A-Z][a-z]*( [A-Z][a-z]*)+$'
    
    for name in names:
        if re.match(pattern, name):
            print(name)
        else:
            print("Invalid name")

check_names(names)