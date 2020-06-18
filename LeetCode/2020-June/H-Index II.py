# The first step is to understand the meaning of H-index.
# 所有论文中（N篇），若是有h篇论文，被引用的次数大于等于h,并且剩余的N-h篇论文的引用次数都小于h。则为h-index。
# Note: [0, 5, 10]这个例子，我们不能说h=0，应该说h为2，因为有两篇论文的引用次数都大于等于2（其实是大于等于5），但是并没有5篇，所以我们要选择2
# [1, 4, 7, 9] 这个例子出错是因为我没有考虑到要选择最大的那个h值（也就是上面所述的），有三篇论文都大于等于3（其实是4），所以我们选择3。用count记录论文数量

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        c_len = len(citations)
        if not c_len:
            return 0
        count = 0
        for i in range(c_len - 1, -1, -1):
            if citations[i] == 0:
                break
            if citations[i] <= (c_len - i):
                # print(citations[i])
                # break
                if count < citations[i]:
                    return citations[i]
                else:
                    return count
            count += 1

        return count

s1 = Solution()
# x = s1.hIndex([0,1,3,5,6])
x = s1.hIndex([1,4,7,9])
print(x)
