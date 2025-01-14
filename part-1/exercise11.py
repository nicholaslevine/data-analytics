def interleave(*lists):
    zipped = zip(*lists)
    return list(zipped)
print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))