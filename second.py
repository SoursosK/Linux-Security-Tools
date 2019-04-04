import os

searchString = input("Please insert the string you want to search for:\n")

os.system("grep -e " + searchString + " /home/*/.bash_history") 
