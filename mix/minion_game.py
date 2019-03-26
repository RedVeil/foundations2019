def minion_game(string):
    vowels = ["A", "E", "I", "O", "U"]
    score_stuart = 0
    score_kevin = 0
    len1 = 1
    test = "AN"
    i = string[-1]

    lst =[]
    # setting up list with single letters
    for i in string:
        lst.append(i)
    print(lst)

    # test for vowels
    for letter in lst:
        if letter in vowels:
            score_kevin += 1
            print(lst["A"])

        else:
            score_stuart +=1

    #
    def add_letter(substring):
        i = substring + string[string.index(substring)+1]
        return i
        if string.index(substring)+1 == len(string)-1:
            return "False"

    print(len(string))
    print(string.index(i))
    print(string[string.index(i)])

    print(add_letter(i))

'''


            #while len1 <= len(string):


    print(score_kevin)
    print(score_stuart)

'''
'''    #print(string[x])
        else:
            score_stuart += 1
            x = string.index(i)+1
            print(string.index(i))
            print(string[string.index(i)])


    #print(score_kevin)
    #print(score_stuart)

'''



minion_game("BANANA")
