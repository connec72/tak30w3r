# Coded By Connec
import os
import time

print("\033[1;31m[\033[1;33m*\033[1;31m]\033[1;32m turkhackteam.org/net")
time.sleep(1)
print("\033[1;31m[\033[1;33m*\033[1;31m]\033[1;32m Gerekli dosyalar kuruluyor...")
time.sleep(1)

# Araçlar
os.system("sudo apt install golang")
os.system("sudo apt install subfinder")
os.system("sudo apt install subjack")
os.system("sudo go install -v github.com/lukasikic/subzy@latest")
os.system("sudo cp /root/go/bin/subzy /usr/bin")

# Modüller


time.sleep(1)
print("\033[1;31m[\033[1;33m*\033[1;31m]\033[1;32m Gerekli dosyalar kuruldu.")
