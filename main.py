import pyfiglet
from colorama import init, Fore, Style
global text1

init()

print("""Choose your font:
1 = Slant
2 = Bulbhead
3 = big""")
choice = input()
choice = int(choice)
if choice == 1:
  text1 = "slant"
if choice == 2:
  text1 = "bulbhead"
if choice == 3:
  text1 = "big"


red= Fore.RED
blue = Fore.BLUE
green = Fore.GREEN
yellow =Fore.YELLOW
cyan = Fore.CYAN
reset = Style.RESET_ALL



print(f"""Choose your colour:
1 = {red}red{reset}
2 = {blue}blue{reset}
3 = {green}green{reset}
4 = {yellow}yellow{reset}
5 = {cyan}cyan{reset}""")
choice = input()
choice = int(choice)
if choice == 1:
  colour = red
if choice == 2:
  colour = blue
if choice == 3:
  colour =green
if choice == 4:
  colour = yellow
if choice == 5:
  colour = cyan

text = input ("What is your desired text?  ")
ascii = pyfiglet.figlet_format(text, font = text1)
print(colour + ascii)
