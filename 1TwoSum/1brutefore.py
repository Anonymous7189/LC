#this is brute force solution to the two sum problem, it has a time complexity of O(n^2) and space complexity of O(1)

def twoSum(nums, target):

    for i in range(len(nums)):

        for j in range(i + 1, len(nums)):

            if nums[i] + nums[j] == target:
                return [i, j]
            
#use the next line to start the function in ur editor


print(twoSum([2,7,11,15], 9))