import math
from collections import deque

def binary_search(list,e):
    low = 0
    high = len(list)-1
    while low<=high:
        mid = math.floor((low+high)/2)
        guess = list[mid]
        if(guess==e):
            return mid
        elif guess>e:
            high = mid-1
        else:
            low = mid+1
    return None

def BFS(graph,my_name,searched_name,result):
    queue = deque()
    checked = []
    queue+=graph[my_name]
    result.append('cxd')
    while(queue):
        name = queue.popleft()
        if(name not in checked):
            if(name==searched_name):
                # result.append(name)
                return True
            else:
                queue+=graph[name]
                checked.append(name)
    return False
