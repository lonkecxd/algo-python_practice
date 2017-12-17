#求最大 分而治之
def find_max(list):
    if(len(list)==0):
        return 0
    n0 = list.pop(0)
    t = find_max(list)
    if(n0>=t):
        return n0
    else:
        return t