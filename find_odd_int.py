def unequal():
    pass

def find_it(seq, z=0):
    t = 0
    x = seq[z]
    count = []
    seq = seq
    print(len(seq))
    while t < len(seq)-1:
        for i in seq:
            t+=1
            if i == x:
                count.append(i)
                print(count)
        if len(count)%2 is not 0:
            print(x)
        else:
            print("equal")
            find_it(seq, z+1)





find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])
