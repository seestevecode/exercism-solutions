"""Implement list functions"""

def append(list1, list2):
    return list1 + list2


def concat(lists):
    result = []
    for item in lists:
        if isinstance(item, list):
            result.extend(item)
        else:
            result.append(item)
    return result


def filter(function, list):
    return [item for item in list if function(item)]


def length(list):
    return sum(1 for item in list)


def map(function, list):
    return [function(item) for item in list]


def foldl(function, list, initial):
    acc = initial
    for item in list:
        acc = function(acc, item)
    return acc
        

def foldr(function, list, initial):
    acc = initial
    for item in list[::-1]:
        acc = function(acc, item)
    return acc


def reverse(list):
    return list[::-1]
