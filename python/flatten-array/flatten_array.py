"""Flatten an arbitrary nested list of sublists and singletons"""

def flatten(iterable):
    result = []
    for item in iterable:
        if isinstance(item, list):
            result.extend(flatten(item))
        elif item is None:
            continue
        else:
            result.append(item)
    return result
