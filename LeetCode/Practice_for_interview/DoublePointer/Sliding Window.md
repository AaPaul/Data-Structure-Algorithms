# Senario
满足XXX条件（计算结果，出现次数，同时包含）

最长/最短

字串/子数组/子序列

Ex.: 长度最小的子数组

# 滑动窗口使用思路
### 寻找最长
核心： 左右双指针（L，R）在起始点，R向右逐位滑动循环
滑动过程中：
- 如果： 窗内元素满足条件，R向右扩大窗口，并更新
- 如果：窗内元素不满足，L向右缩小

直到：R到达结尾
```
Initial: left, right, currResult, bestResult(final answer)

while (right < len(n)) {
    Expand window, add elements at right, update currResult
    while (not satisfied) {
        shrink the window, pop out the element at left (left += 1)
    }
    update bestResult
    right += 1
}

return bestResult
```


### 寻找最短
核心： 左右双指针（L，R）在起始点，R向右逐位滑动循环
滑动过程中：
- 如果：窗内元素满足，L向右缩小，并更新
- 如果： 窗内元素不满足条件，R向右扩大窗口

直到：R到达结尾

```
Initial: left, right, currResult, bestResult(final answer)

while (right < len(n)) {
    Expand window, add elements at right, update currResult
    while (satisfied) {
        update bestResult
        shrink the window, pop out the element at left (left += 1)
    }
    right += 1
}
return bestResult

```