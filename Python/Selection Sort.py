def sort(nums):
    for i in range(5):
        minpos = i
        for j in range(i, 7):
            if nums[j] < nums[minpos]:
                minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

        print(nums)


nums = [2, 5, 8, 3, 9, 1, 7]
sort(nums)
print(nums)
