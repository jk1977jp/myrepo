import subprocess
import shlex
import _winreg

'''
although slightly modified,this script is ported from winenum script (metasploit) and github.com/ankh2054/windows-pentest/blob/master/icacls.bat.
all credit goes to the original authors.
'''


def runcmd(cmd):
	test = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).communicate()
	return test

commands=['systeminfo',
'net view',
'route print',
'ipconfig /displaydns',
'netstat -vb',
'netstat -ns',
'net accounts',
'ipconfig /all',
'arp -a',
'cmd.exe /c set',
'net group administrators',
'net view /domain',
'netsh firewall show config',
'tasklist /svc',
'net localgroup administrators',
'net localgroup',
'net user',
'net group',
'net share',
'net session',
'netsh wlan show networks mode=bssid',
'netsh wlan show drivers',
'gpresult /SCOPE USER /Z',
'gpresult /SCOPE COMPUTER /Z',
'netsh wlan show interfaces',
'netsh wlan show profiles',
'wmic netclient list brief',
'wmic netuse get name,username,connectiontype,localname',
'wmic share get name,path',
'wmic nteventlog get path,filename,writeable',
'wmic netlogin get name,lastlogon,badpasswordcount',
'wmic logicaldisk get description,filesystem,name,size',
'wmic volume list brief',
'wmic group list',
'wmic service list brief',
'wmic useraccount list',
'wmic qfe',
'wmic product get name,version',
'wmic rdtoggle list',
'wmic startup list full'
]

print "[*] This might take a few minutes. please be patient..."

for i in commands:
	try:
		print "[*] Command executing : " + str(i) 
		result = runcmd(i)
		for line in result:
			print line
	except:
		print "ooh, something wrong at..." + str(i)

print "[*] enumerating installed software from different angle..."
print "[*] pleae do not rely on this list solely. you might have to manually check out the host exhaustively"
print "\r\n"

places = ["Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall", "SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall"]

for place in places:
	try:
		key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,place)
		regInfo = _winreg.QueryInfoKey(key)

		item = []
		for i in range(regInfo[0]):
 
			installName = _winreg.EnumKey(key,i)
			try:
				subKey = _winreg.OpenKey(key,installName)
				item.append(_winreg.QueryValueEx(subKey,"DisplayName")[0])
			except:
				pass
		for softwareversion in item:
			print softwareversion
	
	except:
		pass
