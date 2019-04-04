import os

date = input("Please enter a date(format ex. Mar 16): \n")
os.system("last | grep -i '" + date + "'")
