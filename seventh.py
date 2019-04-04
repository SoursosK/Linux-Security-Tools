import os

os.system("getent group sudo | cut -d: -f4 ")
