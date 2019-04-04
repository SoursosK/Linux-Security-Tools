import os

os.system("sudo awk -F\":\" '($2 == \"!\" || $2 == \"*\") {print $1}' /etc/shadow")
os.system("sudo awk -F\":\" '($2 == \"!\" || $2 == \"*\") {passwd $1 -l}' /etc/shadow")
