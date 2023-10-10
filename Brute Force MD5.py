#source: https://gist.github.com/X-88/d3ed3c197086d24eb55be22d5e917632

# -*- coding: utf-8 -*-
#######################################
## App Name: Z-MD5 Brute Force       ##
## Coded by: Zephio                  ##
## Lang: Python 3.xx (QPthon Android ##
## Date : 15-Jun-2019                ##
#######################################
#4 test only
#Zeph: e0acbd6d08021f96c1b90647140f5510
#zeph: 6DC21EDC72C0F66130B270F20F38FAA1
#zep:  4ad0cc43e6a5870cac575f93cb84f522
#ZeP:  1e91560a0224493cef7644dade9ff09c

import os
import time
import hashlib
#Zephio Jun, 2019
#for i in range(256):
    #wl = chr(i)
    #s = format(x, 010')
    
spr = '#######################################'
print(spr)
    
st = time.time()
ofn = "/storage/emulated/0/qpython/zhm_out.txt"
wl = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@#$_&-+()/*":;!?.,~`|•√π÷×¶∆£¢€¥^°={}\%©®™✓[]<>\''
inp = input('MD5 Hash: ')
lpw = int(input('Length of Password: '))
wll = len(wl)
print(spr)
print(' Please Wait...')
print(spr)
    
def ZBruter(n):
    return ((n == 0) and wl[0]) or (ZBruter(n // wll).lstrip(wl[0]) + wl[n % wll])
for i in range(wll ** lpw):
    psw = ZBruter(i).zfill(lpw)
    rc = hashlib.md5(psw.encode('utf-8')).hexdigest()
    print('Index:', hex(i), '/', hex(lpw ** wll), '\nProgress:', (i / ((lpw ** wll) * 100)), '\nPass:', psw, '\nMD5:', rc, '\n'+spr)
    if (rc == inp):
        os.system('clear')
        print(spr, format('\n Coded by: Zephio\n Language: Python (v3xx)\n Status: Done \n Pass: %s \n Pos: %x/%x \n Time: %s S' % (psw, i, wll ** lpw, int(time.time() - st))))
        print(spr)
        break
with open(ofn, 'w') as s:
    s.write('Pass: ' + psw)
s.close()