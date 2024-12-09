import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
args=["-f", "--font"]

def main():

    if len(sys.argv)<2:
        font=random.choice(figlet.getFonts())
        figletize(font)
    if len(sys.argv)>2 and sys.argv[1] in args and sys.argv[2] in figlet.getFonts():
        font=sys.argv[2]
        figletize(font)
    else:
        sys.exit("Invalid usage")



def figletize(f):
    s=input("Input: ")
    figlet.setFont(font=f)
    print(f"Output: {figlet.renderText(s)}")

main()
