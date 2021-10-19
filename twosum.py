#this problem takes in an array of numbers and a target number
#each number in the array is added to another number in the array
#checking all permutations until the target number is reached
#this returns the location of the numbers in the array
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums
        self.target = target
        z = 0
        result=[]


        if len(self.nums)==2:
            return[0,1]

        for x in self.nums:
            z = z + 1
            for y in self.nums[z:]:
                if (x + y) == self.target:
                    a = self.nums.index(x)
                    b = self.nums.index(y)

                    if a == b:
                        
                        reversed_list = self.nums[::-1]
                        first_index_in_reversed = reversed_list.index(y)
                        b = len(self.nums) -1 - first_index_in_reversed

                    result.append(a)
                    result.append(b)
                    return result
