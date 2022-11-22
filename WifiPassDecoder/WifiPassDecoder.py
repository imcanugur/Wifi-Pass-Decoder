'''
    Copyright © 2022 | Uğur CAN
    www.ugurcan.rf.gd
'''

import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

print('*'*50)
print(' '*21+'Uğur CAN')
print('*'*50)
print(' '*18+'Wi-fi Decoder')
print('*'*50)
while True:
    control = input("0: Wi-fi Decoder\n1: Çıkış\nNe Yapmak İstersin: ")
    if control == "0":
        print('*'*50)
        print ("{:<30}**  {:<}".format("Kayıtlı Wi-fi Adı", "Kayıtlı Şifre"))
        print('*'*50)
        for i in profiles:
            try:
                results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
                results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
                try:
            
                    print ("{:<30}->  {:<}".format(i, results[0]))
                    #print (format(i) + " -- " + format(results[0]))
                except IndexError:
                    print ("{:<30}->  {:<}".format(i, ""))
            except subprocess.CalledProcessError:
                print ("{:<30}->  {:<}".format(i, "Şifreye Erişim Reddedildi."))
        print('*'*50)
    elif control == "1":
        break
    else:
        print('*'*50)
        print('Lütfen doğru bir seçim yapın.')
        print('*'*50)