import re

code ="DBMAFAGICPCPHDGIGICPGCGJGOIJODFAIJOCFDIJOBLAALMNIA"

buff=[]

for i in code:
	buff.append(int(hex(ord(i)),16)-0x41)
#print buff

t=""

for j in buff:
	#print '{:04b}'.format(j)
	t +='{:04b}'.format(j)

helloworld =re.findall(".{8}",t)

frame = ""
for  kkk in helloworld:
	frame += hex(int(kkk,2)).replace("0x","\\x")

print frame
