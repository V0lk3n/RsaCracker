#!/usr/bin/env python
# Created by V0lk3n
# Used for RSA challenge.
# Challenge : RSA
# File : auth_channel.txt
# CTF : peaCTF2019

# Install libctf
# git clone https://github.com/arisada/libctf.git
# export PYTHONPATH=/full/path/of/libctf

# Import library
from libctf import *

# Input values
ninput = input("n : ")
n = int(ninput)
einput = input("e : ")
e = int(einput)
cinput = input("c : ")
c = int(cinput)

# Decrypt Cipher
print(inttobytes(RSA(n=n, e=e).encrypt(c)))