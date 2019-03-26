
def base_check(smiley):
    if smiley[0] == ":" or ";":
        if smiley[-1] == "D" or ")":
            return True
        else:
            return False
    else:
        return False
        
#def eye_check(smiley):
    #return

def check_mouth(smiley):
    if smiley[-1] == "D" or ")":
        return True
    else:
        return False


#def check(smiley):
    #if check_mouth(smiley) == True:
        #return "True"




def countSmileys(arr):
    total = 0
    for smiley in arr:
        if base_check(smiley) == True:
            if len(smiley) == 3:
                print("-", smiley)
                if smiley[1] == "-" or "~":
                    if check_mouth(smiley) == True:
                        total += 1
                    else:
                        total +=0
                else:
                    total +=0
            else:
                print(smiley)
                if check_mouth(smiley) == True:
                    #print("-"+smiley)
                    total +=1
                else:
                    total += 0
        else:
             total +=0
    return total



print(countSmileys([':)', ';(', ';}', ':-D']))       # should return 2;
print(countSmileys([';D', ':-(', ':-)', ';~)']))    # should return 3;
print(countSmileys([';]', ':[', ';*', ':$', ';-D'])) # should return 1;


        



