#first half expanding adding .|. reducing -
#second half reducing
# middle line ---WELCOME---
#n lines
# n = odd number
#m (n*3) objects

#str1 = "------------.|.------------"
#str3 = "------------.|.------------"
#print(str1[len(str1)/2])

def doormat(num):
    m = num*3
    x = (m//2)-1
    y = 1
    z = (m//2)-3
    #half=("-"*x + ".|."*y + "-"*x)
    first_half = ""
    welcome = ("-"*z + "WELCOME" + "-"*z+"\n")
    second_half = ""

    def half(x,y):
        return ("-"*x + ".|."*y + "-"*x+"\n")
        
#first half
    for i in range((num//2)):
        first_half+=half(x,y)
        y+=2
        x-=3

    y-=2
    x+=3
#second hlaf
    for i in range((num//2)):
        second_half += half(x,y)
        y-=2
        x+=3



    all=first_half+welcome+second_half
    return all


print(doormat(9))
print(doormat(13))


'''
def doormat(num):
    i = 1
    first_half =
    while i > (num/2):
        return("- /n")
        i+1

print(doormat(5))
'''
