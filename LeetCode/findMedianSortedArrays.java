// My own opinion about this problem is to use quick sort and the time complexity is n(logn) where n is the sum of two arrays.
// However, I think it may exceed the time complexity constrain (log(m+n)). So maybe I need to set a specific function to judge
// if the original array is ordered. The first way successfully passes the test case while I didn't consider the minus test case.
// Finally, this solution is passed.

class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int len1 = nums1.length, len2 = nums2.length;
        int len_total = len1 + len2;
        int [] nums = new int[len_total];
        System.arraycopy(nums1, 0, nums, 0, nums1.length);
        System.arraycopy(nums2, 0, nums, nums1.length, nums2.length);
        double median;
        // Sort
        quickSort(nums, 0, len_total-1);
        if (len_total % 2 == 0) {
            int a = len_total / 2;
            int b = a - 1;
            median = (nums[a] + nums[b]) / 2.0;
        }
        else {
            int a = len_total / 2;
            median = nums [a];
        }
        return median;
    }
    
    void quickSort(int[] a, int left, int right) {
        if (left == right) return;
        int i = left, j = right;
        int flag = a[left];
        int temp;
        while (i != j) {
            while (a[j] >= flag && i != j) j--;
            while (a[i] <= flag && i != j) i++;
            if (i < j) {
            //写的什么**东西，真的想喷自己,下面也是，哪有这么交换两个数的
                //temp = a[j];
                temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
        } 
        temp = a[left];
        a[left] = a[i];
        a[i] = temp;
        if (left < i-1) quickSort(a, left, i-1);
        if (i+1 < right) quickSort(a, i+1, right);
    }
}



// Some summerazition of quick sort:
// 1. 如果选择左基数，必须要从右边开始循环。否则逻辑会不对，尽管可以更改使其正确，但也增加了代码复杂度。

// Referrence
// https://blog.csdn.net/csdnqixiaoxin/article/details/89429528
