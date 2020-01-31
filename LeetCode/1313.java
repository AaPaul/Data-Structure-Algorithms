// 1313. Decompress Run-Length Encoded List
class Solution {
    public int[] decompressRLElist(int[] nums) {
        if (nums.length % 2 != 0 || nums.length < 2 || nums.length > 100) {
            throw new IllegalArgumentException("array is illegal");
        }
        else {
            int[] first = getList(nums[0], nums[1]);
            for (int i = 3; i < nums.length; i += 2) {
                int[] next = getList(nums[i-1], nums[i]);
                first = Concatenate(first, next);
            }
            return first;
        }
    }
    
    public int[] getList(int freq, int val) {
        if (freq > 100 || freq < 1 || val > 100 || val < 1) {
            throw new IllegalArgumentException("elements are illegal");
        }
        int[] lst = new int[freq];
        for (int i = 0; i < freq; i++) {
            lst[i] = val;
        }
        return lst;
    }
    
    public int[] Concatenate(int[] a1, int[] a2) {
        int [] comb = new int[a1.length + a2.length];
        System.arraycopy(a1, 0, comb, 0, a1.length);
        System.arraycopy(a2, 0, comb, a1.length, a2.length);
        return comb;
    }
}

// Note: When defining an array, the format is (int example): int[] arrayName = new int[size];
// It's different with python. "[size]" instead of "(size)".

// python3 version
// actually, i don't need to define the constrains as they have already been existed. 
// list的concatenation，extend是在原list的基础上修改，而comb = comb + lst是相当于重新定义了一个list，把combination放在了叫作comb的list中。
// extend更快。
// Calling the internal functions, the function should be add "self" in function parameter statement.在括号里要声明self，要不然会报错：该函数未声明
/*
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        comb = []
        i = 1
        while i < len(nums):
            lst = self.getList(nums[i-1], nums[i]) # 用self调用函数
            comb.extend(lst) # comb+=lst
            i = i+2
        return comb
             
    def getList(self, freq, val):
        lst = []
        for i in range(freq):
            lst.append(val)
        return lst
 */           
