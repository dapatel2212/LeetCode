'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

class Solution:
    def twoSum(self,nums,target):
        li = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    print("The two numbers that add up to the target are:", nums[i], "and", nums[j])
                    li.append(i)
                    li.append(j)
        print(li)
        return li   

Sol = Solution()
list = eval(input("Enter the list of numbers: "))
target = int(input("Enter the target number: "))
result = Sol.twoSum(list,target)
print("The indices of the two numbers that add up to the target are:", result)