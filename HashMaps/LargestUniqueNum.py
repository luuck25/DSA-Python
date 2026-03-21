


def largest_uni_num(nums):

    freq = {}

    for num in nums:
        freq[num] = freq.get(num,0)+1

    largest_num = float('-inf')

    for num in nums:

        if freq[num] == 1:
            largest_num = max(largest_num,num)

    return -1 if largest_num == float('-inf') else largest_num
          

