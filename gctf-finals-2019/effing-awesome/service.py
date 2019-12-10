#!/usr/bin/env python3
import os
import sys
import pty
import subprocess
import termios
import signal
import threading

print(r'''
_________________________________.__
\_   _____/\_   _____/\_   _____/|__| ____    ____
 |    __)_  |    __)   |    __)  |  |/    \  / ___\
 |        \ |     \    |     \   |  |   |  \/ /_/  >
/_______  / \___  /    \___  /   |__|___|  /\___  /
        \/      \/         \/            \//_____/
        GoogleCTF 2019  - isn't this fun?
'''.strip())


class Reader(threading.Thread):
    def __init__(self, input, output):
        super(Reader, self).__init__()
        self.input = input
        self.output = output

    def run(self):
        try:
            b = b''
            while b'>>> >>> >>> >>> ... ... >>> ' not in b:
              b += os.read(self.input, 1)

            while True:
                c = os.read(self.input, 1)
                if c == '':
                    break
                os.write(self.output, c)
        except:
            pass


master, slave = pty.openpty()
p = subprocess.Popen(['python3'], stdin=slave, stdout=slave, stderr=subprocess.DEVNULL)
os.close(slave)

os.write(master, b'''
forbidden  = [input, print, chr, ord, type, locals, compile, repr, globals]
forbidden += [setattr, memoryview, exec, __import__, eval ]
for f in forbidden:
  delattr(__builtins__, f.__name__)

del forbidden
''')

new = termios.tcgetattr(master)
new[3] &= ~termios.ECHO
termios.tcsetattr(master, termios.TCSANOW, new)

def handle_alarm(meh, meh2):
    print('meh')
    p.kill()
    sys.exit(0)


signal.signal(signal.SIGALRM, handle_alarm)
#signal.alarm(15)

Reader(master, sys.stdout.fileno()).start()

i = 0
try:
  while True:
    c = os.read(0, 1)
    i += 1

    if i > 2048:
        print('too much data')
        p.kill()
        break

    if c == b'':
        os.close(master)
        break

    if c not in b' !"#$%&\'()*+,-./:;<=>?@f[\\]^_`{|}~\n\r':
        continue

    os.write(master, c)
except:
    p.kill()
finally:
    p.wait()
