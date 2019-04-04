import os
import sys
import crypt


username = input("Please insert username:\n")
password = input("Password should contain atlease 6 characters, upper and lowercase, digit, one of the special characters #$!@%!\nPlease insert password:\n")

if len(password) < 6:
	print("	Error! Password contains less that 6 characters")
	sys.exit(0)
elif not(any(x.isupper() for x in password) and any(x.islower() for x in password)):
	print("	Error! Password must contain atlease one uppercase and one lowercase character")
	sys.exit(0)
elif not(any(x.isdigit() for x in password)):
	print("	Error! Password must contain atlease one number")
	sys.exit(0)
elif not(any((x in set('#$!@%')) for x in password)):
	print("	Error! Password must contain atlease one special character")
	sys.exit(0)

group = input("Please insert user group:\n")
description = input("please insert a description:\n")

EncryptedPassword = crypt.crypt(password, "sdf#@$12398s")
os.system("useradd -p " + EncryptedPassword + " -m -d /home/" + username + " -g " + group + " -c " + description + " " + username)
