from pwn import *

data = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
for i in range(256):
    potential_flag = str(xor(bytes.fromhex(data), i))
    if potential_flag[2] == 'c':
        print(potential_flag)