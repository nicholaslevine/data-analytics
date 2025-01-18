def extract_numbers(string):
    words = string.split()
    finalnums = []
    for word in words:
        try:
            num = int(word)
        except ValueError:
            try:
                num = float(word)
            except ValueError:
                continue
        finalnums.append(num)
    return finalnums

print(extract_numbers("abd 123 1.2 test 13.2 -1"))            