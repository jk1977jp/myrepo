#!/usr/bin/python

# understanding the alphanumeric shellcode concept

'''

[i] going to split each hex in the shellcode in 2 part. For example, 0x31 is going to be 0011/0001 in bin. then, add 0x41 for converting to chars

['00110001', '11000000', '01010000', '01101000', '00101111', '00101111', '01101100', '01110011', '01101000', '00101111', '01100010', '01101001', '01101110', '10001001', '11100011', '01010000', '10001001', '11100010', '01010011', '10001001', '11100001', '10110000', '00001011', '11001101', '10000000']


[['0011', '0001'], ['1100', '0000'], ['0101', '0000'], ['0110', '1000'], ['0010', '1111'], ['0010', '1111'], ['0110', '1100'], ['0111', '0011'], ['0110', '1000'], ['0010', '1111'], ['0110', '0010'], ['0110', '1001'], ['0110', '1110'], ['1000', '1001'], ['1110', '0011'], ['0101', '0000'], ['1000', '1001'], ['1110', '0010'], ['0101', '0011'], ['1000', '1001'], ['1110', '0001'], ['1011', '0000'], ['0000', '1011'], ['1100', '1101'], ['1000', '0000']]

printing obfuscated chars

DBMAFAGICPCPGMHDGICPGCGJGOIJODFAIJOCFDIJOBLAALMNIA


alpha shellcode

0x44,0x42,0x4d,0x41,0x46,0x41,0x47,0x49,0x43,0x50,0x43,0x50,0x47,0x4d,0x48,0x44,0x47,0x49,0x43,0x50,0x47,0x43,0x47,0x4a,0x47,0x4f,0x49,0x4a,0x4f,0x44,0x46,0x41,0x49,0x4a,0x4f,0x43,0x46,0x44,0x49,0x4a,0x4f,0x42,0x4c,0x41,0x41,0x4c,0x4d,0x4e,0x49,0x41,
[Finished in 0.1s]
'''


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