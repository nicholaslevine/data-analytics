def reverse_dictionary(d):
    result = {}
    for key, values in d.items(): 
        for value in values:  
            result[value] = key 
    return result

d = {
    'move': ['liikuttaa'],
    'hide': ['piilottaa', 'salata'],
    'six': ['kuusi'],
    'fir': ['kuusi']
}
print(reverse_dictionary(d))
