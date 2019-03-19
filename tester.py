import itertools

xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
#Test.assert_equals(choose_best_sum(230, 4, xs), 230)
#Test.assert_equals(choose_best_sum(430, 5, xs), 430)
#Test.assert_equals(choose_best_sum(430, 8, xs), None)


def choose_best_sum(t, k, ls):
    comb = itertools.combinations(ls, k)
    sum_distance = []
    for i in comb:
        distance = sum(i)
        sum_distance.append(distance)
    #print(sum_distance)
    



choose_best_sum(230, 4, xs)
