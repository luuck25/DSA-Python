
def subset(nums):

    def subsets(index,path):

        if index == len(nums):
            result.append(path[:])
            return

        path.append(nums[index])
        subsets(index+1,path)
        path.pop()
        subsets(index+1,path)

    result = []

    subsets(0,[])


    return result    

print(subset([1,2,3]))
    