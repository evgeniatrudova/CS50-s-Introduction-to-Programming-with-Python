# pwd
# cd +(output from pwd)
# ls
# touch adieu.py
# code adieu.py
# add in your names
# CTRL + D to get the list with added in names

import sys

def main():
    names = []
    try:
        while True:
            name = input("Name: ")
            names.append(name)
    except EOFError:
        pass

    if len(names) == 1:
        print(f"Adieu, adieu, to {names[0]}")

    elif len(names) == 2:
        print(f"Adieu, adieu, to {names[0]} and {names[1]}")

    else:
        farewell = ", ".join(names[:-1]) + f", and {names[-1]}"
        print(f"Adieu, adieu, to {farewell}")

if __name__ == "__main__":
    main()
