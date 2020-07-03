# iteration and recursive are both a kind of loop. However, in the case with a big number of loop
# the efficiency of iteration must be higher than the latter one.

from typing import List


class Solution:
    def change(self, cells: List[int]) -> List[int]:
        copy = [0] * 8
        for i in range(1, 7):
            copy[i] = int(cells[i - 1] == cells[i + 1])
        return copy

    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        # This directory is to mark the length of loop (iteration length would be marked in the key value)
        iterations = {}
        for i in range(N):
            cells_str = str(cells)
            if cells_str in iterations:
                it_len = i - iterations[cells_str]
                return self.prisonAfterNDays(cells, (N - i) % it_len)
            else:
                iterations[cells_str] = i
                cells = self.change(cells)

        return cells


s1 = Solution()
res = s1.prisonAfterNDays([1, 0, 0, 1, 0, 0, 1, 0], 7)
print(res)
