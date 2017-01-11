def diff(l1):
    return list(set(l1))

def intersect(l1, l2):
    return list(set(l1) & set(l2))

def union(l1, l2):
    return list(set(l1) | set(l2))

def test():
    l1 = [1,2,3,4,5,9,11,15]
    l2 = [4,5,6,7,8]
    l3 = []
    assert(diff(l1) == [1,2,3,4,5,9,11,15])
    assert(intersect(l1, l2) == [4,5])
    assert(diff(l3) == [])
    assert(intersect(l1, l3) == [])
    print('passed')

if __name__ == '__main__':
    test()
