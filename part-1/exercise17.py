def positive_list(nums):
    positives = list(filter(lambda x: x > 0, nums))
    return positives

print(positive_list([2, -2, 0, 1, -7]))