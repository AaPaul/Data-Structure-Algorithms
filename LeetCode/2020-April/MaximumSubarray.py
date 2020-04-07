import sys


def maxSubArray(nums: list):
    result = maxArray(nums, 0, len(nums) - 1)
    print(result)
    # return result


def maxArray(nums, start, end):
    # This statement is very important
    if start == end:
        return nums[start]
    mid = (start + end) // 2
    # return max(maxArray(nums, start, mid),
    #            maxArray(nums, mid + 1, end),
    #            maxCrossMid(nums, start, end, mid))

    m1 = maxArray(nums, start, mid)
    m2 = maxArray(nums, mid + 1, end)
    m3 = maxCrossMid(nums, start, end, mid)
    maximum = max(m1, m2, m3)
    return maximum


def maxCrossMid(nums, start, end, mid):
    left_max = nums[mid]
    sum_eles = 0

    # Calculate the min in the left of the mid point including mid point
    for i in range(mid, start - 1,
                   -1):  # range(n, m, -1) From n to (m+1) in the reverse order, the length of step is 1.
        sum_eles += nums[i]
        if sum_eles > left_max:
            left_max = sum_eles

    # Calculate the min in the right of the mid point
    sum_eles = 0
    right_max = nums[mid+1]

    # Note: I have a mistake here. I just use range(end - mid) as the loop condition
    # which is absolutely wrong.
    # Another mistake, I use (end - mid + 1) as the start point, (end - 1) as the stop point.
    # These 2 mistakes show that I don't understand the meaning of the function
    # actually we only need know it just start from (mid + 1)

    for i in range(mid + 1, end + 1, 1):
        sum_eles += nums[i]
        if sum_eles > right_max:
            right_max = sum_eles

    return right_max + left_max


# maxSubArray([1, 2])
# maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
maxSubArray([0, -3, 1, 1])

# When dealing with the part of dividing the list, I forgot to handle the situation that
# the program has to deal with the list with 1 element
# So there is an error that recursionError.

# Another notation. In leetCode, I need built-in function to support me to submit the result.

"""
range()
Example:
range(0, 10, 1)
start from 0, stop at 10 excluding 10, the step is 1

range(10, 0, -1)
start from 10, stop at 1, the step is -1.
"""