def threeSum(nums) :
    result = []
    nums = sorted(nums)
    if len(nums) < 2:
        return result
    if nums[0] > 0:
        return result
    for i in range(len(nums) -2):
        target = -nums[i]
        if i > 0 and nums[i] == nums[i-1]:
            continue
        j = i + 1
        k = len(nums) - 1
        while j < k:
            sum = nums[j]+ nums[k]
            if sum == target:
                result.append([nums[i], nums[j], nums[k]])
                while j<k and nums[j] == nums[j+1]:
                    j+=1
                while j<k and nums[k-1] == nums[k]:
                    k-=1
                j+=1
                k-=1
            elif sum < target:
                while j<k and nums[j] == nums[j+1]:
                    j+=1
                j+=1
            elif sum > target:
                while j<k and nums[k-1] == nums[k]:
                    k-=1
                k-=1
    return result


print(threeSum([-1, 0, 1, 2, -1, -4]))




