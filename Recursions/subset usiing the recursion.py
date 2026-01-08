def subsets(lst):
    if not lst:
        return [[]]
    result = subsets(lst[1:])
    return result + [subset + [lst[0]] for subset in result]
print(subsets([1, 2, 3]))
l=[1]
a=l[1:]
print(a)

