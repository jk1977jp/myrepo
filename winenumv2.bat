REM borrowed from metasploit module(winenum) and slightly modified. all credit goes to the original author.

whoami /all
systeminfo
netstat -nao
net view
route print
ipconfig /displaydns
netstat -vb
netstat -ns
net accounts
ipconfig /all
arp -a
cmd.exe /c set
net group administrators
net view /domain
netsh firewall show config
tasklist /svc
tasklist /m
net localgroup administrators
net localgroup
net user
net group
net share
net session
netsh wlan show networks mode=bssid
netsh wlan show drivers
gpresult /SCOPE USER /Z
gpresult /SCOPE COMPUTER /Z
netsh wlan show interfaces
netsh wlan show profiles
reg query "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall" /s | findstr "\<DisplayName"
reg query "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall" /s | findstr "DisplayName"
reg query HKLM /f password /t REG_SZ /s
reg query HKCU /f password /t REG_SZ /s

@echo off
REM wmic commands 
wmic /APPEND:wmic.txt netclient list brief /format 
wmic /APPEND:wmic.txt netuse get name,username,connectiontype,localname
wmic /APPEND:wmic.txt share get name,path
wmic /APPEND:wmic.txt nteventlog get path,filename,writeable
wmic /APPEND:wmic.txt netlogin get name,lastlogon,badpasswordcount
wmic /APPEND:wmic.txt logicaldisk get description,filesystem,name,size
wmic /APPEND:wmic.txt volume list brief
wmic /APPEND:wmic.txt group list
wmic /APPEND:wmic.txt service list full / format:list
wmic /APPEND:wmic.txt useraccount list
wmic /APPEND:wmic.txt qfe
wmic /APPEND:wmic.txt product get name,version
wmic /APPEND:wmic.txt rdtoggle list
wmic /APPEND:wmic.txt startup list full


REM borrowed from github.com/ankh2054/windows-pentest/blob/master/icacls.bat. all credit goes to the original author. 
REM Description: Script that queries all services and searches for exeuctables that give the Everyone group RW access.
REM Type: Incorrect file permissions
REM Note: The ^ characters escapes certain characters that brerak the FOR loop.
REM Note: tokens=1* - The value at the first delimeter and everything after. 
for /f "tokens=1*" %%m in ('sc query state^= all ^| find "SERVICE_NAME"') do (
    for /f "tokens=1* delims=: " %%r in ('sc qc "%%~n" ^| find "BINARY_PATH_NAME"') do (
        for /f "delims=" %%x in ('echo(%%~s^| findstr /L /V /I /C:"%SystemRoot%\System32" /C:"%SystemRoot%\SysWOW64"') do (
            icacls "%%~x"
        )
    )
)


