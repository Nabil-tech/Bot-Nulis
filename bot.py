import requests
import shutil
import os
import json
import itertools
import threading
import time
import sys
G = '\033[92m'
Y = '\033[93m'
R = '\033[91m'
B = '\033[1m'
W = '\033[0m'

done = False

 
url="https://tools.zone-xsec.com/api/nulis.php?q="
logo=f"""{R}
╲╲╲╲╲┏━━━┓╱╱╱╱╱
╲┏━━━┻━━━┻━━━┓╱     "{W}    Bot Nulis{R}"
╲┃╭━╮┏━━━┓╭━╮┃╱  "{W} ====================={R}"
╱┃┃╳┃┣◯-◯┫┃╳┃┃╲
╱┃╰━╯┣━━━┫╰━╯┃╲  "{W} Author : NBL CODE{R}"
╱┃┈▊▊▊▊┈▂▃▅▇┈┃╲   "{W}Versi  : 0.01{R}"
╱┗━━━━━━━━━━━┛╲
"""
def ketik(teks):
 for i in teks + "\n":
  sys.stdout.write(i)
  sys.stdout.flush()
  time.sleep(0.1)
   
ketik("WELCOME TO MY SCRIPT")
    
username = "Nabil" 
password = "0101010111011010" 

def login (user_name, pass_word) :
    if user_name != username and pass_word != password :
        hasil = False
    else :
        hasil = True

    return hasil

i=5
while i>=1:
    print (f'{G}link username & password: {W}https://sfile.mobi/3trX1GQEFyD')
    userName_=input(f'{Y}masukan username anda :')
    password_=input(f'{Y}masukan password :')
    hasil=(login(userName_, password_))
    if hasil == True :
        print (f'{G}login user berhasil') 
        break
    else :
        i-=1
        print('gagal login, sisa percobaan login adalah :', i )        
def biasa():
    tulis=input("masukan tulisan: ")
    req=requests.get(url+tulis)
    jeson=json.loads(req.text)
    link=jeson['image']
    image_url= link
    nama_file = image_url.split("/")[-1]
    r = requests.get(image_url, stream = True)
    if r.status_code == 200:
        r.raw.decode_content = True
        with open(nama_file,'wb') as f:
            shutil.copyfileobj(r.raw, f)
            print('Berhasil, Cek file dengan nama:',nama_file)
    else:
        print('Terjadi Kesalahan')

def file():
    tulis=input("nama file: ")
    try:
        file=open(tulis, "r").read()
    except IOError:
        print("file tidak ada")
    ubah=file.replace(" ", "%20")
    cek=ubah.replace("\n", "%0A")
    req=requests.get(url+cek)
    jeson=json.loads(req.text)
    link=jeson['image']
    image_url= link
    nama_file = image_url.split("/")[-1]
    r = requests.get(image_url, stream = True)
    if r.status_code == 200:
        r.raw.decode_content = True
        with open(nama_file,'wb') as f:
            shutil.copyfileobj(r.raw, f)
            print('Berhasil, Cek Gambar dengan Nama:',nama_file)
    else:
        print('Terjadi Kesalahan')

if __name__=="__main__":
    os.system("clear")
    print(logo)
    print(f'{G}1. Tulis Biasa')
    print("2. Tulis Lewat File")
    print("0. Kembali")
    pil=input(f'{W}Metode => ')
    if pil == "1":
        biasa()
    elif pil == "2":
        file()
    else:
        print(pil, "tidak ada")