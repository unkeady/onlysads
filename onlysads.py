from os import system, name
from pytube import YouTube
from sys import platform
from time import sleep
import urllib.request
import argparse
import re
import os

des = "YIRMAA GİDİYOM AAA KİKİK İK İK İK İKAAAAAAA"



filepath = 'C:/Users/unkeady/Documents/GitHub/onlysads/docs/itag.txt'

windowsdesktop = "C:/Users/unkeady/Desktop"
windowsdocuments = "C:/Users/unkeady/Documents"
windowsdownloads = "C:/Users/unkeady/Downloads"

linuxdesktop = "/mnt/c/Users/unkeady/Desktop"
linuxdocuments = "/mnt/c/Users/unkeady/Documents"
linuxdownloads = "/mnt/c/Users/unkeady/Downloads"

searchtimes = 1





def banner():
    print('''                                           
                     __                     __          
        ____  ____  / /_  ___________ _____/ /____      
       / __ \/ __ \/ / / / / ___/ __ `/ __  / ___/      
      / /_/ / / / / / /_/ (__  ) /_/ / /_/ (__  )       
      \____/_/ /_/_/\__, /____/\__,_/\__,_/____/        
                   /____/                               
                                                    ''')
    sleep(2)
    clear()



def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')



def bye():
    clear()
    print("I don't like goodbyes if you're leaving then get the fuck.")
    exit()



def gitgud():
    print('''
       |^^^|
        }_{
        }_{
    /|_/---\_|\ 
    I _|\_/|_ I
    \| |   | |/
       | G |
       | I |
       | T |
       |   |
       | G |
       | U |
       | D |
       |   |
       \   /
        \ /
         Y
    ''')
    sleep(2)
    clear()


def description(finalurl):
    yt = YouTube(str(finalurl))
    print(f'Title ~ {yt.title}')
    print(f'Length ~ {yt.length} seconds')
    print(f'Rating ~ {yt.rating}')
    print(f'Views ~ {yt.views}')
    print(f'Author ~ {yt.author}')
    print(f'Date ~ {yt.publish_date}')
    input("\n ~ press enter ~")
    clear()

    while True:
        print('1 ~ Go to download')
        print('2 ~ Show description')
        print('3 ~ Thumbnail url')
        print('4 ~ Download thumbnail')
        print('0 ~ alt f4')

        cat = input("> ")

        if (cat.lower() == "1"):
            clear()
            download(yt)

        elif (cat.lower() == "2"):
            clear()
            print(f'{yt.description}')
            input("\n ~ press enter ~")
            clear()

        elif (cat.lower() == "3"):
            clear()
            print(f'Thumbnail > {yt.thumbnail_url}')
        
        elif (cat.lower() == "4"):
            clear()
            thumbnaildown(yt.thumbnail_url)
        
        elif (cat.lower() == "0"):
            bye()
        
        else:
            clear()
            print("Bir daha dene! Seni şanslı araba! Fırlat!")


def search():
    word = input("> ")
    url = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + word)
    shorturl = re.findall(r"watch\?v=(\S{11})", url.read().decode())

    i = 0
    while (i < searchtimes):
        yt = YouTube(str("https://www.youtube.com/watch?v=" + shorturl[i]))
        print('[', i, '] ', f'{yt.title} - {yt.author}', sep='')
        i = i + 1

    take = int(input("\n> "))
    finalurl = ("https://www.youtube.com/watch?v=" + shorturl[take])
    clear()
    description(finalurl)




def thumbnaildown(theurl):
    while True:
        print('  ~ Location ~ \n')
        print('1 ~ Desktop')
        print('2 ~ Downloads')
        print('3 ~ Documents')
        print('4 ~ Enter location')
        print('0 ~ alt f4')

        cat = input("> ")

        if (cat.lower() == "1"):
            clear()
            print("  ~ downloading ~  ")
            urllib.request.urlretrieve(theurl, desktop + "/thumbnail.jpg")
            clear()
            print("   ~ finished ~  ")
            break

        elif (cat.lower() == "2"):
            clear()
            print("  ~ downloading ~  ")
            urllib.request.urlretrieve(theurl, downloads + "/thumbnail.jpg")
            clear()
            print("   ~ finished ~  ")
            break

        elif (cat.lower() == "3"):
            clear()
            print("  ~ downloading ~  ")
            urllib.request.urlretrieve(theurl, documents + "/thumbnail.jpg")
            clear()
            print("   ~ finished ~  ")
            break

        elif (cat.lower() == "4"):
            clear()
            dest = input("Enter a destination like > C:/Users/unkeady/Desktop/thumbnail.jpg\n> ")
            print("  ~ downloading ~  ")
            urllib.request.urlretrieve(theurl, str(dest))
            clear()
            print("   ~ finished ~  ")
            break

        elif (cat.lower() == "0"):
            bye()
        else:
            clear()
            print("Bir daha dene! Seni şanslı araba! Fırlat!")


def download(yt):

    while True:
        print('1 ~ Download highest quality')
        print('2 ~ Video + Audio')
        print('3 ~ Video')
        print('4 ~ Audio')
        print('5 ~ Show all options')
        print('0 ~ alt f4')

        cat = input("> ")

        if (cat.lower() == "1"):
            clear()
            down = yt_obj.streams.get_highest_resolution()
            downloadmenu(down)

        elif (cat.lower() == "2"):
            clear()
            itag('2', yt)

        elif (cat.lower() == "3"):
            clear()
            itag('3', yt)

        elif (cat.lower() == "4"):
            clear()
            itag('4', yt)

        elif (cat.lower() == "5"):
            clear()
            itag('5', yt)

        elif (cat.lower() == "0"):
            bye()

        else:
            clear()
            print("Bir daha dene! Seni şanslı araba! Fırlat!")


def itag(test, yt):

    global itagdown
    itagdown = []
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        i = 0
        while line:
            itag = line[:line.find('-')]
            if yt.streams.get_by_itag(int(itag)):
                if int(test) == 5:
                    itaginfo = line[line.find('-')+3:]
                    print('[', i, '] ', itaginfo, end='', sep='')
                    itagdown.append(itag)
                    i = i + 1
                elif int(test) == int(line[line.index('-') + 1: line.index('-') + 2]):
                    itaginfo = line[line.find('-')+3:]
                    print('[', i, '] ', itaginfo, end='', sep='')
                    itagdown.append(itag)
                    i = i + 1
            line = fp.readline()
            cnt += 1

    cat = input('>')
    if cat == 99:
        clear() #AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        download(yt)
    downloadmenu(yt.streams.get_by_itag(itagdown[int(cat)]))


        


def downloadmenu(down):
    clear()
    while True:
        print('  ~ Location ~ ')
        print('1 ~ Desktop')
        print('2 ~ Downloads')
        print('3 ~ Set location')
        print('0 ~ alt f4')

        loc = input("> ")

        if (loc.lower() == "1"):
            clear()
            print("  ~ downloading ~  ")
            down.download(desktop)
            clear()
            print("   ~ finished ~  ")

        elif (loc.lower() == "2"):
            clear()
            print("  ~ downloading ~  ")
            down.download(downloads)
            clear()
            print("   ~ finished ~  ")

        elif (loc.lower() == "3"):
            clear()
            dest = input("Enter a destination\n> ")
            print("  ~ downloading ~  ")
            down.download(str(dest))
            clear()
            print("   ~ finished ~  ")
            break

        elif (loc.lower() == "0"):
            clear()
            bye()
        else:
            clear()
            print("Bir daha dene! Seni şanslı araba! Fırlat!")


def running():

    clear()
    banner()
    while True:

        print('1 ~ Search')
        print('2 ~ Link')
        print('3 ~ ffmpeg')
        print('0 ~ alt f4')

        ready = input("> ")

        if (ready.lower() == "1"):
            clear()
            search()
        elif (ready.lower() == "2"):
            clear()
            urlgo = input("url > ")
            description(urlgo)
        elif (ready.lower() == "3"):
            clear()
        elif(ready.lower() == "gitgud"):
            gitgud()
        elif (ready.lower() == "0"):
            clear()
            bye()
        else:
            clear()
            print("Bir daha dene! Seni şanslı araba! Fırlat!")







itagdown = list()

if platform == "linux" or platform == "linux2":
    desktop = linuxdesktop
    documents = linuxdocuments
    downloads = linuxdownloads
if platform == "win32":
    desktop = windowsdesktop
    documents = windowsdocuments
    downloads = windowsdownloads





parser = argparse.ArgumentParser(description = des)
parser.add_argument('-r', '--run', action='store_true', help="BURN BABY BURN!")
parser.add_argument('-d', '--download', help="Download the video")


args = parser.parse_args()



try:
    if args.run:
        running()
    if args.download:
        yt_obj = YouTube(str(args.download))
        yt_obj.streams.get_highest_resolution().download(desktop)

except:
    print('Argparse error.')
    pass



