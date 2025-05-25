def two_sum(nums: list, target: int)-> list[int]:
    length = len(nums)
    if length < 2:
        return [-1]
    for i in range(length):
        for j in range(i+1, length):
            if nums[i] + nums[j] == target:
                return [i, j]
    
    return [-1]

print(two_sum([2,7,11,15], 9))