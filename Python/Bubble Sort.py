def sort(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp


nums = [3, 5, 7, 2, 4, 8, 1, 9]
sort(nums)

print(nums)