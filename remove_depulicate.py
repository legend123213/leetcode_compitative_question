def removeDuplicates(nums):
    i = 0
    j = 1
    while j != len(nums):
        if nums[i] != nums[j] and j - i != 1:
            i += 1
            nums[i] = nums[j]
            j += 1
        elif nums[i] != nums[j] and j - i == 1:
            i += 1
            j += 1
        else:
            j += 1
        if j == len(nums):
            break

    nums = nums[: i + 1]
    return len(nums)


