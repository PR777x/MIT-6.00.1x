
L1 = [1,2,3,4]
L2 = [1,2,5,6]

def removeDups(L1, L2):
    L1Start = L1[:]
    for e1 in L1Start:
        if e1 in L2:
            L1.remove(e1)
