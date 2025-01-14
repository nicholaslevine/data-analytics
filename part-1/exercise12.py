def distinct_characters(strings):
    stringsDict = {}
    for string in strings:
        distinct = len(set(string))
        stringsDict[string] = distinct
    return stringsDict
print(distinct_characters(["check", "look", "try", "pop"]))