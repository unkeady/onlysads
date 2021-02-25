from colorama import Fore as f, Back as b, Style as s, init
from os import system, name
from pytube import YouTube
from sys import platform
from time import sleep
import urllib.request
import argparse
import re


des = "onlysads"

searchtimes = 10
filepath = 'docs/itag.txt'

init(autoreset=True)  # colorama

if platform == "linux" or platform == "linux2":
    desktop = "/mnt/c/Users/unkeady/Desktop"
    documents = "/mnt/c/Users/unkeady/Documents"
    downloads = "/mnt/c/Users/unkeady/Downloads"
if platform == "win32":
    desktop = "C:/Users/unkeady/Desktop"
    documents = "C:/Users/unkeady/Documents"
    downloads = "C:/Users/unkeady/Downloads"


def banner():
    print(f.RED + s.BRIGHT + '''
                     __                     __          
        ____  ____  / /_  ___________ _____/ /____      
       / __ \/ __ \/ / / / / ___/ __ `/ __  / ___/      
      / /_/ / / / / / /_/ (__  ) /_/ / /_/ (__  )       
      \____/_/ /_/_/\__, /____/\__,_/\__,_/____/        
                   /____/                               
                                                        ''')

    sleep(1)
    clear()


def running():

    clear()
    banner()
    while True:

        print(f.MAGENTA + '1 ~ Search')
        print(f.GREEN + '2 ~ Link')
        print(f.CYAN + '3 ~ Color test')
        print(f.RED + '0 ~ Exit')

        ready = input(f.MAGENTA + '> ' + s.RESET_ALL)

        if (ready.lower() == "1"):
            clear()
            search()
        elif (ready.lower() == "2"):
            clear()
            urlgo = input("url > ")
            clear()
            description(urlgo)
        elif (ready.lower() == "3"):
            clear()
            print(f.BLACK + "BLACK")
            print(f.RED + "RED")
            print(f.GREEN + "GREEN")
            print(f.YELLOW + "YELLOW")
            print(f.BLUE + "BLUE")
            print(f.MAGENTA + "MAGENTA")
            print(f.CYAN + "CYAN")
            print(f.WHITE + "WHITE")
            print(f.RESET + "RESET\n")
        elif (ready.lower() == "0"):
            clear()
            bye()
        else:
            clear()
            print("running error")


def search():
    word = input(f.MAGENTA + '> ' + s.RESET_ALL)
    url = urllib.request.urlopen(
        "https://www.youtube.com/results?search_query=" + word)
    shorturl = re.findall(r"watch\?v=(\S{11})", url.read().decode())

    i = 0
    while (i < searchtimes):
        yt = YouTube(str("https://www.youtube.com/watch?v=" + shorturl[i]))
        print(f.BLUE + '[', f.BLUE + str(i), f.BLUE + '] ',
              f.GREEN + f'{yt.title} - {yt.author}', sep='')
        i = i + 1

    take = int(input(f.MAGENTA + '\n> ' + s.RESET_ALL))
    finalurl = ("https://www.youtube.com/watch?v=" + shorturl[take])
    clear()
    description(finalurl)


def description(finalurl):
    yt = YouTube(str(finalurl))
    print(f.BLUE + f'Title ~ {yt.title}')
    print(f.BLUE + f'Length ~ {yt.length} seconds')
    print(f.BLUE + f'Rating ~ {yt.rating}')
    print(f.BLUE + f'Views ~ {yt.views}')
    print(f.BLUE + f'Author ~ {yt.author}')
    print(f.BLUE + f'Date ~ {yt.publish_date}')
    input(f.RED + "\n ~ press enter ~\n" + s.RESET_ALL)
    clear()

    while True:
        print(f.MAGENTA + '1 ~ Go to download')
        print(f.GREEN + '2 ~ Show description')
        print(f.CYAN + '3 ~ Thumbnail url')
        print(f.YELLOW + '4 ~ Download thumbnail')
        print(f.RED + '0 ~ Exit')

        cat = input(f.MAGENTA + '> ' + s.RESET_ALL)

        if (cat.lower() == "1"):
            clear()
            download(yt)

        elif (cat.lower() == "2"):
            clear()
            print(f.BLUE + f'{yt.description}')
            input(f.RED + "\n ~ press enter ~\n" + s.RESET_ALL)
            clear()

        elif (cat.lower() == "3"):
            clear()
            print(f.BLUE + f'Thumbnail > {yt.thumbnail_url}\n')

        elif (cat.lower() == "4"):
            clear()
            thumbnaildown(yt.thumbnail_url)

        elif (cat.lower() == "0"):
            bye()

        else:
            clear()
            print("description error")


def thumbnaildown(theurl):
    while True:
        print(f.RED + '  ~ Location ~ \n')
        print(f.MAGENTA + '1 ~ Desktop')
        print(f.GREEN + '2 ~ Downloads')
        print(f.CYAN + '3 ~ Documents')
        print(f.YELLOW + '4 ~ Enter location')
        print(f.RED + '0 ~ Exit')

        cat = input(f.MAGENTA + '> ' + s.RESET_ALL)

        if (cat.lower() == "1"):
            clear()
            print(f.GREEN + "  ~ downloading ~  ")
            urllib.request.urlretrieve(theurl, desktop + "/thumbnail.jpg")
            clear()
            print(f.GREEN + "   ~ finished ~  ")
            break

        elif (cat.lower() == "2"):
            clear()
            print(f.GREEN + "  ~ downloading ~  ")
            urllib.request.urlretrieve(theurl, downloads + "/thumbnail.jpg")
            clear()
            print(f.GREEN + "   ~ finished ~  ")
            break

        elif (cat.lower() == "3"):
            clear()
            print(f.GREEN + "  ~ downloading ~  ")
            urllib.request.urlretrieve(theurl, documents + "/thumbnail.jpg")
            clear()
            print(f.GREEN + "   ~ finished ~  ")
            break

        elif (cat.lower() == "4"):
            clear()
            dest = input(
                "Enter a destination like > C:/Users/unkeady/Desktop/thumbnail.jpg\n> ")
            print(f.GREEN + "  ~ downloading ~  ")
            urllib.request.urlretrieve(theurl, str(dest))
            clear()
            print(f.GREEN + "   ~ finished ~  ")
            break

        elif (cat.lower() == "0"):
            bye()
        else:
            clear()
            print("thumbnaildown error")


def download(yt):

    while True:
        print(f.MAGENTA + '1 ~ Download highest quality')
        print(f.GREEN + '2 ~ Video + Audio')
        print(f.CYAN + '3 ~ Video')
        print(f.YELLOW + '4 ~ Audio')
        print(f.MAGENTA + '5 ~ Show all options')
        print(f.RED + '0 ~ Exit')

        cat = input(f.MAGENTA + '> ' + s.RESET_ALL)

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
            print("download error")


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
                    print(f.BLUE + '[', f.BLUE + str(i), f.BLUE +
                          '] ', f.GREEN + itaginfo, end='', sep='')
                    itagdown.append(itag)
                    i = i + 1
                elif int(test) == int(line[line.index('-') + 1: line.index('-') + 2]):
                    itaginfo = line[line.find('-')+3:]
                    print(f.BLUE + '[', f.BLUE + str(i), f.BLUE +
                          '] ', f.GREEN + itaginfo, end='', sep='')
                    itagdown.append(itag)
                    i = i + 1
            line = fp.readline()
            cnt += 1

    print(f.RED + "\n ~ enter for back ~ ")
    cat = input(f.MAGENTA + '> ' + s.RESET_ALL)
    if cat == "":
        clear()
        download(yt)
    downloadmenu(yt.streams.get_by_itag(itagdown[int(cat)]))


def downloadmenu(down):
    clear()
    while True:
        print(f.RED + '  ~ Location ~ ')
        print(f.MAGENTA + '1 ~ Desktop')
        print(f.GREEN + '2 ~ Downloads')
        print(f.CYAN + '3 ~ Set location')
        print(f.RED + '0 ~ Exit')

        loc = input(f.MAGENTA + '> ' + s.RESET_ALL)

        if (loc.lower() == "1"):
            clear()
            print(f.GREEN + "  ~ downloading ~  ")
            down.download(desktop)
            clear()
            print(f.GREEN + "   ~ finished ~  ")
            sleep(2)
            running()

        elif (loc.lower() == "2"):
            clear()
            print(f.GREEN + "  ~ downloading ~  ")
            down.download(downloads)
            clear()
            print(f.GREEN + "   ~ finished ~  ")
            sleep(2)
            running()

        elif (loc.lower() == "3"):
            clear()
            dest = input(f.RED + "Enter a destination\n> ")
            print(f.GREEN + "  ~ downloading ~  ")
            down.download(str(dest))
            clear()
            print(f.GREEN + "   ~ finished ~  ")
            sleep(2)
            running()

        elif (loc.lower() == "0"):
            clear()
            bye()
        else:
            clear()
            print("downloadmenu error")


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def bye():
    clear()
    print("I don't like goodbyes if you're leaving then get the fuck.")
    exit()


parser = argparse.ArgumentParser(description=des)
parser.add_argument('-r', '--run', action='store_true', help="run the program")
parser.add_argument('-d', '--download', help="Download the video")
args = parser.parse_args()

try:
    if args.run:
        running()
    if args.download:
        yt_obj = YouTube(str(args.download))
        yt_obj.streams.get_highest_resolution().download(desktop)
        clear()
        print(f.GREEN + "   ~ finished ~  ")

except:
    print('Task failed succesfuly.')
    pass
