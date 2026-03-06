# Remove Duplicates from Sorted Array
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
# Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.
# The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.
class Solution:
    def removeDuplicates(arr):
        j=0
        for i in range(1,len(arr)):
            if arr[j]!=arr[i]:
                j+=1
                arr[j]=arr[i]
        return j+1
    
 
    x=[1,2,2,2,3,3,3,4,4,5]   
     
    print(f"The unique elements are {removeDuplicates(x)}")


# j = 0This is your "Slow Pointer." It marks the position of the last unique element found so far. 
# We start at 0 because the first element is always unique by default.
# for i in range(1, len(nums)):This is your "Fast Pointer" (the scout). It starts at index 1 and scans through the rest of the array 
# looking for values that are different from what we've already seen.
# if nums[j] != nums[i]:The scout ($i$) compares its current value to the last unique value we saved at ($j$).
# If they are the same, it's a duplicate! The scout just moves on.If they are different, it means we found a new unique number.
# j += 1 Since we found a new unique number, we move our "Slow Pointer" one spot forward to make room for it.
# nums[j] = nums[i] We take the new unique number found by the scout ($i$) and copy it into the new position ($j$). 
# This effectively "overwrites" the old duplicates.
# return j + 1 Because indices start at 0, the "Slow Pointer" $j$ represents the index. To get the total count (length) of unique items,
#  we add 1.