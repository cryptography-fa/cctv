# Decompiled By xNot_Found
# Github : https://github.com/hatakecnk
# uncompyle6 version 3.3.5
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Jul  7 2019, 21:05:54) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: <seni>
import LIST
from LIST.id import *
from LIST.ia import *
from LIST.il import *
from LIST.us import *
from LIST.au import *
from LIST.kr import *
from LIST.bn import *
from LIST.cn import *
from LIST.jp import *
from LIST.my import *
from LIST.ps import *
from LIST.sg import *
from LIST.th import *
from LIST.vn import *
import requests, re, os
b = '\x1b[0;34m'
p = '\x1b[0;35m'
g = '\x1b[1;32m'
w = '\x1b[1;37m'
r = '\x1b[1;31m'
y = '\x1b[1;33m'
cyan = '\x1b[0;36m'
lgray = '\x1b[0;37m'
dgray = '\x1b[1;30m'
ir = '\x1b[0;101m'
reset = '\x1b[0m'

def main():
    os.system('clear')
    print '\x1b[0;34m#########################'
    print '\x1b[0;34m#  \x1b[1;31mT00L : scan cctv V.1 \x1b[0;34m#'
    print '\x1b[0;34m#  \x1b[1;33mCODE : MR.B3604      \x1b[0;34m#'
    print '\x1b[0;34m#  \x1b[1;32mTEAM : 407 A3X       \x1b[0;34m#'
    print '\x1b[0;34m#  \x1b[0;36mYT   : GUNAWAN ID    \x1b[0;34m#'
    print '\x1b[0;34m#########################'
    print '\x1b[0mSilahkan Pilih Nomer Di Bawah Ini ^_^'
    print '\x1b[1;32m [1] Indonesia'
    print '\x1b[1;33m [2] Jepang'
    print '\x1b[1;32m [3] Korea'
    print '\x1b[1;33m [4] China'
    print '\x1b[1;32m [5] Malaysia'
    print '\x1b[1;33m [6] Singapura'
    print '\x1b[1;32m [7] Amerika'
    print '\x1b[1;33m [8] Palestina'
    print '\x1b[1;32m [9] Israel'
    print '\x1b[1;33m [10] Vietnam'
    print '\x1b[1;32m [11] Thailand'
    print '\x1b[1;33m [12] Australia'
    print '\x1b[1;32m [13] India'
    print '\x1b[1;33m [14] Brunei'
    print '\x1b[1;32m [15] Cara pemakaian'
    print '\x1b[1;33m [0] Exit'
    select = input('\x1b[0mMasukan Nomer Pilihan Kalian : ')
    filtering(select)


def filtering(pilih):
    if pilih == 1:
        indonesia()
    elif pilih == 2:
        jepang()
    elif pilih == 3:
        korea()
    elif pilih == 4:
        cina()
    elif pilih == 5:
        malaysia()
    elif pilih == 6:
        singapura()
    elif pilih == 7:
        amerika()
    elif pilih == 8:
        palestina()
    elif pilih == 9:
        israel()
    elif pilih == 10:
        vietnam()
    elif pilih == 11:
        thailand()
    elif pilih == 12:
        australia()
    elif pilih == 13:
        india()
    elif pilih == 14:
        brunei()
    elif pilih == 15:
        print p + '[1] Silahkan Pilih Nomer Yang Kalian Inginkan' + w
        print r + '[2] Nanti kalian Akan mendapatkan IP Dan Port cctv' + w
        print y + '[3] Kalian Copy IP Dan Port cctv Tersebut' + w
        print g + '[4] Selanjutnya Kalian Pastekan Di Google' + w
        print b + '[5] Selamat Mencoba ^_^' + w
    elif pilih == 0:
        print r + 'Tidak Ada Yang Tidak Mungkin Di Dunia Ini' + w
        print y + 'jangan lupa subscribe channel gua !!' + w
        print g + 'Makasih !!' + w
        os.sys.exit()
    else:
        print r + 'Exiting ...' + w
        os.sys.exit()


if __name__ == '__main__':
    main()