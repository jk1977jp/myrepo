#!/usr/bin/python

# understanding the alphanumeric shellcode concept

import re

data="\x31\xc0\x50\x68\x2f\x2f\x6c\x73\x68\x2f\x62\x69\x6e\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80"

buff = ['{:08b}'.format(i) for i in bytearray(data)]

test = [(re.findall(".{4}",j)) for j in buff]

print test
final = []
for k,v in test:
	final.extend ([hex(int(k,2) + 0x41), hex(int(v,2) + 0x41)])

alphanumeric_encoded = ""
obfuscated_chars =""
for shellcode in final:
	obfuscated_chars += chr(int(shellcode,16))
	alphanumeric_encoded += shellcode+","
#	.replace("0x", "\\x")


print obfuscated_chars
print alphanumeric_encoded