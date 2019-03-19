import sys

seq = []
returns = []

def input_fields(num):
    num = int(num)
    t = 0
    while t < num:
        seq.append(input("= "))
        t+=1

def ip4(string):
    splitted4=string.split(".")
    print(splitted4)
    if len(splitted4) == 4:
        for i in splitted4:
            if int(i) <= 254:
                returns.append("IPv4")
            else:
                returns.append("Neither")
    else:
        returns.append("Neither")


def ip6(string):
    splitted6=string.split(".")
    print(splitted6)
    if len(splitted6) == 8:
        for i in splitted6:
            if i.ishex() or i.isdecimal():
                returns.append("IPv6")
            else:
                returns.append("Neither")
    else:
        returns.append("Neither")


def ip_check(seq):
    N = int(len(seq))
    t = 0
    while t < N:
        if ":" in seq[t]:
            ip6(seq[t])
            t+=1
        elif "." in seq[t]:
            ip4(seq[t])
            t+=1
        else:
            returns.append("Neither")
            t+=1



a=input("- ")
input_fields(a)
ip_check(seq)
print("\n".join(returns))

'''print(ip_check("7\n""1050:1000:1000:a000:5:600:300c:326b\n""1050:1000:2000:ab00:5:600:300c:326a\n"
"1050:1000:3000:abc0:5:600:300c:326c\n"
"1051:1000:4000:abcd:5:600:300c:326b\n"
"22.231.113.64\n"
"22.231.113.16\n"
"222.231.113.64\n"))

#print(ip_check("35\n"
"1050:0:0:0:5:600:300c:326b\n"
"1050:0:0:0:5:600:300c:326a\n"
"1050:0:0:0:5:600:300c:326c\n"
"1051:0:0:0:5:600:300c:326b\n"
"22.231.113.64\n"
"22.231.113.164\n"
"255.231.111.64\n"
"253.231.111.64\n"
"1050:10:0:0:5:600:300c:326b\n"
"1050:10:0:0:5:600:300c:326a\n"
"1050:10:0:0:5:600:300c:326c\n"
"1051:10:0:0:5:600:300c:326b\n"
"22.21.113.61\n"
"22.21.113.162\n"
"255.21.111.63\n"
"253.21.111.69\n"
"1050:10:0:0:15:600:300c:326b\n"
"1050:10:0:10:5:600:300c:326a\n"
"1050:10:10:0:5:600:300c:326c\n"
"1051:110:0:0:5:600:300c:326b\n"
"22.211.113.64\n"
"22.212.113.164\n"
"255.213.111.64\n"
"253.214.111.64\n"
"1050:10:0:0:15:600:300c:326k\n"
"1050:10:0:0:15:600:300c:326g\n"
"1050:10:0:0:15:600:300c:326h\n"
"1050:10:0:0:15:600:300c:326i\n"
"22.211.113.364\n"
"22.212.113.3164\n"
"255.213.111.464\n"
"253.214.111.564\n"
"not an ip address\n"
"not an ipv4 Address\n"
"Not an IPv5 Address\n"))


"7\n"
"1050:1000:2000:ab00:5:600:300c:326a\n"
"1050:1000:3000:abc0:5:600:300c:326c\n"
"1051:1000:4000:abcd:5:600:300c:326b\n"
"22.231.113.64\n"
"22.231.113.16\n"
"222.231.113.64\n"'''
