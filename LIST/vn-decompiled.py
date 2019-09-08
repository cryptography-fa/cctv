# Decompiled By xNot_Found
# Github : https://github.com/hatakecnk
# uncompyle6 version 3.3.5
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Jul  7 2019, 21:05:54) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: <seni>
import requests, os, re
b = '\x1b[0;34m'
g = '\x1b[1;32m'
w = '\x1b[1;37m'
r = '\x1b[1;31m'
y = '\x1b[1;33m'
cyan = '\x1b[0;36m'
lgray = '\x1b[0;37m'
dgray = '\x1b[1;30m'
ir = '\x1b[0;101m'
reset = '\x1b[0m'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def vietnam():
    res = requests.get('https://www.insecam.org/en/bycountry/VN/', headers=headers)
    findpage = re.findall('"?page=",\\s\\d+', res.text)[1]
    rfindpage = findpage.replace('page=", ', '')
    os.system('clear')
    print '\x1b[0;34m#########################'
    print '\x1b[0;34m#  \x1b[1;31mT00L : scan cctv V.1 \x1b[0;34m#'
    print '\x1b[0;34m#  \x1b[1;33mCODE : MR.B3604      \x1b[0;34m#'
    print '\x1b[0;34m#  \x1b[1;32mTEAM : 407 A3X       \x1b[0;34m#'
    print '\x1b[0;34m#  \x1b[0;36mYT   : GUNAWAN ID    \x1b[0;34m#'
    print '\x1b[0;34m#########################'
    print ('{}{}Daftar Halaman : {} {}').format(r, y, rfindpage, r)
    run()


def run():
    try:
        page = input('\x1b[0;37mPilih Halaman : ')
        url = 'https://www.insecam.org/en/bycountry/VN/?page=' + str(page)
        print '\x1b[1;30m~ DONE :* ~'
        res = requests.get(url, headers=headers)
        findip = re.findall('http://\\d+.\\d+.\\d+.\\d+:\\d+', res.text)
        count = 1
        for _ in findip:
            hasil = findip[count]
            print ('{}=> {}{} {}').format(dgray, g, hasil, dgray)
            count += 1

    except:
        print cyan + 'Copy Salah Satu Dan Pastekan Di Google' + w