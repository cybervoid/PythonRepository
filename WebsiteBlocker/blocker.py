
#Edit host file to redirect a url
#/etc/hosts/
import os
import platform

myOs = platform.system()
host_path = "x"
if myOs.lower() = "Windows".lower():
    host_path=r"C:\Windows\System32\drivers\etc\hosts\"
else:
    host_path = "/etc/hosts/"

redirect = "127.0.0.1"

website_list = ["www.foxnews.com", "facebook.com", "msnbc.com", "www.msnbc.com"]
#setup infinite loop
#while True:
