from subprocess import run
from time import sleep

print('Creating a .vbs file...')
sleep(1)

file = open(r'C:\Users\Arman\Desktop\Github\hacking\virus\virus.vbs', "w+")

print('Writing the Message...')
sleep(1)

file.writelines([
    'msgbox "Uyarı sistemde virüs tespit edildi. Hata Kodu: 80091273E ", 52 ,  "Uyarı"\n',
    'For x = 1 To 10\n',
    '\t msgbox "Dosyalar Taranıyor...", 50 , "Uyarı"\n',
    'Next\n',
    'DO\n',
    'msgbox "Sistem ele geçirildi. Dosyalar Aktarılıyor...", 16 ,"Uyarı"\n',
    'LOOP\n'])

file.close()

res = run(r'cscript C:\Users\Arman\Desktop\Github\hacking\virus\virus.vbs')