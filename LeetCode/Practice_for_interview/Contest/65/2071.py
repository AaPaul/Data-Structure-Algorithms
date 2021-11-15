from sortedcontainers import SortedList 
import bisect

class Solution:
    def maxTaskAssign(self, tasks, workers, pills, strength):
        tasks = sorted(tasks)
        workers = sorted(workers)

        def check(k):
            W = SortedList(workers[-k:])
            # W = list(workers[-k:])
            tries = pills

            for elem in tasks[:k][::-1]:
                # place = W.bisect_left(elem)
                place = bisect.bisect_left(W, elem)
                if place < len(W):
                    W.pop(place)
                elif tries > 0:
                    # place2 = W.bisect_left(elem - strength)
                    place2 = bisect.bisect_left(W, elem - strength)
                    if place2 < len(W):
                        W.pop(place2)
                        tries -= 1
                else:
                    return False

            return len(W) == 0

        beg, end = 0, min(len(workers), len(tasks)) + 1
        while beg + 1 < end:
            mid = (beg + end)//2
            if check(mid):
                beg = mid
            else:
                end = mid

        return beg

s= Solution()
tasks = [3,2,1]
workers = [0,3,3]
pills = 1
strength = 1
print(s.maxTaskAssign(tasks, workers, pills, strength))