#!/usr/bin/env python
# Created By V0lk3n
# Used for RSA challenge.
# Challenge : RSA
# File : enc_channel.txt
# CTF : peaCTF2019

# Factorise n for have p and q values
# https://www.alpertron.com.ar/ECM.HTM

# Install libctf
# git clone https://github.com/arisada/libctf.git
# export PYTHONPATH=/full/path/of/libctf

#import library
from libctf import *

#modInv function
def extendedEuclid(a, b):
        x,y, u,v = 0,1, 1,0
        while a != 0:
                q, r = b//a, b%a
                m, n = x-u*q, y-v*q
                b,a, x,y, u,v = a,r, u,v, m,n
        return b, x, y

def modInv(a, m):
        """returns the multiplicative inverse of a in modulo m as a
           positive value between zero and m-1"""
        # notice that a and m need to co-prime to each other.
        linearCombination = extendedEuclid(a, m)
        return linearCombination[1] % m

#input value
ninput = input("n : ")
n = int(ninput)
einput = input("e : ")
e = int(einput)
cinput = input("c : ")
c = int(cinput)
pinput = input("p : ")
p = int(pinput)
qinput = input("q : ")
q = int(qinput)
p*q == n

# Found opposite e modulo n
phi = (p-1)*(q-1)

d = modInv(e, phi)

# Decrypt cipher
pt = pow(c, d, n)

# Print the flag
print(inttobytes(pt))
