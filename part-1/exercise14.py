def find_matching(list, search):
    result = []
    for i in range(len(list)):
        if (search in list[i]):
            result.append(i)
    return result
print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"));



