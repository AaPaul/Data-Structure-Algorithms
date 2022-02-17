class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j, summ, carry = len(a) - 1, len(b) - 1, "", 0
        while i >= 0 or j >= 0 or carry:
            d1 = int(a[i]) if i >= 0 else 0
            d2 = int(b[j]) if j >= 0 else 0
            summ += str((d1 + d2 + carry) % 2)
            carry = (d1 + d2 + carry) // 2
            i, j = i-1, j-1
        return summ[::-1]

# C++ version
'''
class Solution {
public:
    string addBinary(string a, string b) {
        string res = "";
        int carry = 0;//进位
        int i = a.size()-1, j = b.size()-1;
        while(i>=0 || j>=0 || carry==1)
        {
            int sum = carry;
            if(i>=0)
                sum += (a[i--]-'0');
            if(j>=0)
                sum += (b[j--]-'0');
            res = to_string(sum%2) + res;
            carry = sum/2;
        }
        return res;
    }
};

'''