"""
low = 0, high = nums.length

mid = low + (high - low) // 2, we don't use (low + high) // 2 as there may be an overflow because of additive.

Template:
public int binarySearch(int[] nums, int key) {
    int l = 0, h = nums.length - 1;
    while (l <= h) {
        int m = l + (h - l) / 2;
        if (nums[m] == key) {
            return m;
        } else if (nums[m] > key) {
            h = m - 1;
        } else {
            l = m + 1;
        }
    }
    return -1;
}

We should care about the boundry problem. Sometime the loop condition should be (low < high), or in the loop, (high = m). 
"""
# Because the condition is low <= high, therefore after the loop, high must be lower than low. We are supposed to return high
class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        while low <= high:
            mid = low + (high - low) // 2
            squre = int(mid * mid)
            if squre == x:
                return mid
            if squre > x:
                high = mid - 1
            else:
                low = mid + 1
        return high