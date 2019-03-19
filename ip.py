import sys

class IP:
    def __init__(self):
        self.ip4 = 0
        self.ip6 = 0
        self.seq = []


    def input_fields(self,num):
        num = int(num)
        t = 0
        while t < num:
            self.seq.append(input("= "))
            t+=1
        self.ip_selector(self.seq)
        #print(seq)


    def ip_selector(self, seq):
        for i in seq:
            #if i[4] is ":":
                #ip6(i)
            if "." in i:
                self.ip4_funct(i)
                #print("ip")
            else:
                self.printer()



    def ip4_funct(self, ip):
        ip_blocks = ip.split(".")
        #print(ip_blocks)
        if len(ip_blocks) is 4:
            for block in ip_blocks:
                #print(block)
                if int(block) <= 254:
                    self.ip4 = 1
                    #print("ip4")
                else:
                    #print("else")
                    self.ip4 = 0
                    break
        self.printer()


    def ip6_funct(self, ip):
        pass

    def printer(self):
        if self.ip4 == 1:
            print("IPv4")
        #elif ip6 == 1:
            #print("IPv6")
        else:
            print("Neither")


#if __name__ is "__name__":
a=input("- ")
test = IP()
test.input_fields(a)
