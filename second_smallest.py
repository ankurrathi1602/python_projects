# To find the Second smallest number from the list

def sec_small(l):

    a1, a2 = l[0], l[0]
    for i in l:
        if a1 >= i:
            a1, a2 = i, a1
        elif a2 > i:
            a2=i
    return a2
print(sec_small([1, 2, -8, -2, 0]))
