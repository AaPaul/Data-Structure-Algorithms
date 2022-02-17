class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return [1]
        # digits[-1] += 1
        # if digits[-1] == 10:
        #     digits[-1] = 0
        flag = 1
        for i in range(len(digits) - 1, -1, -1):
            temp = digits[i] + flag
            if temp == 10:
                digits[i] = 0
            else:
                digits[i] = temp
                flag = 0
                break

        if flag == 1:
            digits.insert(0, 1)

        return digits

# Another method
# We can calculate the number of 9 from the last one (from right to left), then we only need to
# change the list with the corresponding number.