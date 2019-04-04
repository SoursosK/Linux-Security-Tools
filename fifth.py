import os

print("Server info:")
os.system("uname -a")
print("\nTime since last reboot:")
os.system("who -b")
print("\nLogged in users' info:")
os.system("w")
