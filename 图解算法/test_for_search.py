from 图解算法 import search_algorithms as search

#二分查找
ordered_list = [1,2,4,5,7,9]
print(search.binary_search(ordered_list,7))

#广度搜索
friendsGraph = {
    'cxd':['syq','asd'],
    'syq':['cxd','rty'],
    'asd':['cxd'],
    'rty':['cxd','syq']
}
result = []
print(search.BFS(friendsGraph,'cxd','rty',result))
print(result)