


def sum(nums):
    nums1 = []

    for i in range(len(nums)):
        sum = 0
        if i == 0:
            sum = nums[i] + nums[i+1]
        elif i == len(nums) -1:
            sum = nums[i-1] + nums[i]     
        else:
            sum = nums[i-1] + nums[i] + nums[i+1]

        nums1.append(sum)    

    return nums1


print(sum([4, 0, 1, -2, 3]))
