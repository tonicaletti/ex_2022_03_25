from math import floor

def twoCitySchedCost(costs) -> int:

    def f(arr):
        return max(arr) - min(arr)

    def bubbly(nums):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if f(nums[j]) < f(nums[i]):
                    nums[i], nums[j] = nums[j], nums[i]
        return nums


    sortednums = bubbly(costs)

    print("sorted: ", sortednums)
    idx_a = 0
    idx_b = 0
    cost_sum = 0

    each = floor(len(costs)/2)
    print("each ", each)
    i = 0

    while(idx_a < each and idx_b < each):
        if sortednums[i][0] < sortednums[i][1]:
            idx_a += 1
            cost_sum = cost_sum + sortednums[i][0]
        else:
            idx_b += 1
            cost_sum = cost_sum + sortednums[i][1]
        i = i +1

    if idx_a == each:
        while i < len(sortednums):
            cost_sum = cost_sum + sortednums[i][1]
            i = i +1
    if idx_b == each:
        while i < len(sortednums):
            cost_sum = cost_sum + sortednums[i][0]
            i = i +1

    return cost_sum

twoCitySchedCost([[345,2], [346,3], [1,234], [4,324], [1345,2], [3,888]])
