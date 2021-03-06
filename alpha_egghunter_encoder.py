
import itertools
import pprint


'''
helper script for 'Hand-crafting the encoder'
explanation at "https://www.corelan.be/index.php/2010/01/09/exploit-writing-tutorial-part-8-win32-egg-hunting/ "
               "QuickZip Stack BOF 0day: a box of chocolates"
'''

alpha_shellfriendly = [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47,48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68,
                       69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
                       90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108,
                       109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]


def reverse(line_of_shellcode):
    for chunk in range(0,len(bytearray(line_of_shellcode)),2):
        yield line_of_shellcode[chunk:chunk+2]
    

def twoscomplement(value):
    
    if value >= 1<<31:
        value -= 1<<32

    return str(hex(value)).lstrip("-0x").rstrip("L")


def combination(c):
    for x,y,z in itertools.product(alpha_shellfriendly,repeat=3):
        if sum((x,y,z)) == c and (x == y== z or x == y or y == z ):
            yield map(hex,(x,y,z)), map(chr,(x,y,z))


shellcode_string = "AF75EAAF"
hex_value =0xAFEA75AF
c=0x151

try:
    reverse_test = [i for i in reverse(shellcode_string)]
    print "[+] reversed :" + str(reverse_test[::-1])
    print "[+] hex value: 0x" + "".join(reverse_test[::-1])
    
    test = twoscomplement(hex_value)
    print "[+] 2scomplement : " + test

    combi = [l for l in combination(c) ]
    print "useful combinations "
    pprint.pprint( combi)
except:
    pass
