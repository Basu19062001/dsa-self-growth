def two_sum(nums: list, target: int)->list[int]:
    length = len(nums)
    if length < 2:
        return [-1]
    index_map={}
    for i in range(length):
        complement = target - nums[i]
        if complement in index_map and index_map[complement] != i:
            return [index_map[complement], i]
        index_map[nums[i]] = i

    return [-1]


print(two_sum([2,17,11,7,15],9))
