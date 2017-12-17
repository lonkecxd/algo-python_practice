import math
# 选择排序 selection_sort
def selection_sort(list):
    def getsmallestIndex(list):
        sm = list[0]
        sm_index = 0
        for i in range(len(list)):
            if(sm>list[i]):
                sm = list[i]
                sm_index = i
        return sm_index

    result = []
    for i in range(len(list)):
        sm = getsmallestIndex(list)
        result.append(list.pop(sm))

    return result

#快速排序
def quick_sort(list):
    if(len(list)<=1):
        return list
    baseline = list.pop(0)
    list1 = [i for i in list if(i<=baseline)]
    list2 = [i for i in list if(i>baseline)]
    return quick_sort(list1)+[baseline]+quick_sort(list2)