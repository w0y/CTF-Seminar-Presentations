#!/usr/bin/env python3
from z3 import *

# Challenge
#BINARY = "0110011011011110001111000001101111111000011111111101111111001111"

# deadbeef
BINARY = "01110011111111111110001110111000"

# Array of 64 Z3 bool variables
length = len(BINARY)
bits = [Bool(i) for i in range(length)]

# Returns the neighbors of a bit
def neighbors(x):
    return bits[(x - 1) % length], bits[x], bits[(x + 1) % length]

# Rules for input == 0
def false(x):
    a, b, c = neighbors(x)
    return Or(And(a, b, c), And(Not(a), Not(b), Not(c)))

# Rules for input == 1
def true(x):
    a, b, c = neighbors(x)
    return Or(And(a, b, Not(c)), 
              And(a, Not(b), c), 
              And(a, Not(b), Not(c)), 
              And(Not(a), b, c), 
              And(Not(a), b, Not(c)), 
              And(Not(a), Not(b), c))

# Add rules to solver
s = Solver()
for i in range(0, length):
    s.add(true(i) if BINARY[i] == "1" else false(i))

# Generate all solutions. Add negated model to formula to avoid duplicates.
while(s.check() == sat):
    m = s.model()
    res = "".join(map(lambda x: "1" if m[x] else "0", bits))
    s.add(Not(And([x == m[x] for x in bits])))
    print("%x" % int(res, 2))
