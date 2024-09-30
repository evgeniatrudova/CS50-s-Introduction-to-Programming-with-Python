import sys
import pyfiglet
import random

# terminal instructions
# 1) pip install pyfiglet
# 2) pip show pyfiglet
# 3) python figlet.py
available_fonts = pyfiglet.FigletFont.getFonts()

def main():
    if len(sys.argv) not in [1, 3]:
        sys.exit("Invalid usage")
    font = None
    if len(sys.argv) == 3:
        if sys.argv[1] in ["-f", "--font"]:
            font = sys.argv[2]
            if font not in available_fonts:
                sys.exit("Invalid usage")
        else:
            sys.exit("Invalid usage")

    if font is None:
        font = random.choice(available_fonts)

    text = input("Input: ")

    figlet = pyfiglet.Figlet(font=font)
    ascii_art = figlet.renderText(text)

    print(ascii_art)

if __name__ == "__main__":
    main()
