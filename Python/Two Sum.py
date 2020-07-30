class Solution:
    # Approach - 1 : Brute Force O(N)
    def brute_twoSum(self, nums,k):

        for i in range(len(nums)-1):
            for j in range(i,len(nums)):
                if nums[j]+nums[i]==k:
                    return True

        return False
    # Approach - 2 : Using "in" keyword of python
    def in_twoSum(self, nums,k):

        for i in range(len(nums)):
            if k-nums[i] in nums:
                return True

        return False

    # Approach - 3 : Two pointer technique
    def pointer_twoSum(self,nums,k):
        nums.sort()
        l,r=0,len(nums)-1# Errors exist

class Solution:
    # Approach - 1 : Brute Force O(N)
    def brute_twoSum(self, nums,k):

        for i in range(len(nums)-1):
            for j in range(i,len(nums)):
                if nums[j]+nums[i]==k:
                    return [nums[i],nums[j]]

        return -1
    # Approach - 2 : Using "in" keyword of python
    def in_twoSum(self, nums,k):

        for i in range(len(nums)):
            if k-nums[i] in nums:
                return [nums[i],k-nums[i]]

        return -1

    # Approach - 3 : Two pointer technique
    def pointer_twoSum(self,nums,k):
        nums.sort()
        l,r=0,len(nums)-1
        while(l<r):
            x=nums[l]+nums[r]
            if x==k:
                return [nums[l],nums[r]]
            elif x>k:
                r-=1
            else:
                l+=1
        return -1

    # Approach - 3 : Hashmap

    def hash_twoSum(self, nums,target):
        complement ={}
        for i,v in enumerate(nums):
            if v in complement:
                return complement[v],i
            else:
                complement[target - v] = i
        return -1
    
sol = Solution()
print(sol.brute_twoSum([1, 3, 8, 2],10))
print(sol.brute_twoSum([3, 9, 13, 7],8))
print(sol.brute_twoSum([4, 2, 6, 5, 2],4))
print(sol.brute_twoSum([3,2,4],6))



print(sol.in_twoSum([1, 3, 8, 2],10))
print(sol.in_twoSum([3, 9, 13, 7],8))
print(sol.in_twoSum([4, 2, 6, 5, 2],4))
print(sol.in_twoSum([3,2,4],6))



print(sol.pointer_twoSum([1, 3, 8, 2],10))
print(sol.pointer_twoSum([3, 9, 13, 7],8))
print(sol.pointer_twoSum([4, 2, 6, 5, 2],4))
print(sol.pointer_twoSum([3,2,4],6))


print(sol.hash_twoSum([1, 3, 8, 2],10))
print(sol.hash_twoSum([3, 9, 13, 7],8))
print(sol.hash_twoSum([4, 2, 6, 5, 2],4))
print(sol.hash_twoSum([3,2,4],6))



        while(l<r):
            x=nums[l]+nums[r]
            if x==k:
                return True
            elif x>k:
                r-=1
            else:
                l+=1
        return False
    
sol = Solution()
print(sol.brute_twoSum([1, 3, 8, 2],10))
print(sol.brute_twoSum([3, 9, 13, 7],8))
print(sol.brute_twoSum([4, 2, 6, 5, 2],4))


print(sol.in_twoSum([1, 3, 8, 2],10))
print(sol.in_twoSum([3, 9, 13, 7],8))
print(sol.in_twoSum([4, 2, 6, 5, 2],4))


print(sol.pointer_twoSum([1, 3, 8, 2],10))
print(sol.pointer_twoSum([3, 9, 13, 7],8))
print(sol.pointer_twoSum([4, 2, 6, 5, 2],4))

