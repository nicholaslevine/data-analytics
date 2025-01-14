def transform(str1, str2):
    words1 = str1.split(" ")
    words2 = str2.split(" ")
    ints1 = map(int, words1)
    ints2 = map(int, words2)
    combined = zip(ints1, ints2)
    products = list(map(lambda tuple: tuple[0] * tuple[1], combined))
    return products
print(transform("1 5 3", "2 6 -1"))


