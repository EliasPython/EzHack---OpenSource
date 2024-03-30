# Imports ------

import quit
import function3
try:
	import function2
except:
	print("fnc2: Not loaded")

# Imports-end----


# Main printing 
print('''
 /$$$$$$$$           /$$   /$$                     /$$      
| $$_____/          | $$  | $$                    | $$      
| $$       /$$$$$$$$| $$  | $$  /$$$$$$   /$$$$$$$| $$   /$$
| $$$$$   |____ /$$/| $$$$$$$$ |____  $$ /$$_____/| $$  /$$/
| $$__/      /$$$$/ | $$__  $$  /$$$$$$$| $$      | $$$$$$/ 
| $$        /$$__/  | $$  | $$ /$$__  $$| $$      | $$_  $$ 
| $$$$$$$$ /$$$$$$$$| $$  | $$|  $$$$$$$|  $$$$$$$| $$ \  $$
|________/|________/|__/  |__/ \_______/ \_______/|__/  \__/
	 ''' )
print("---------------------------------------------------------------")
print("EzHack made by Elias")
print("Discord Contact: eliasmw7")
print("OpenSource project legal hacking tool")
print("---------------------------------------------------------------")

# Option
print("- 1 - Credits")
print("- 2 - quit")
print("- 0 - null") # Unused
print("- 0 - null") # Unused
print("- 0 - null") # Unused
print("- 0 - null") # Unused
print("---------------------------------------------------------------")


#Others
option = input("Option:")
def nsc():
    with open('function2.py', 'r') as file:
        code = file.read()
    exec(code)



# If statements
if option == 1:
	function3.crd()
if option == 2:
	quit.quit()
else:
	print("?ERROR?: Inavlid option")
