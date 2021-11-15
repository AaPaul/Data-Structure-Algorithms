class Solution(object):
    def decodeCiphertext1(self, encodedText, rows):
        """
        :type encodedText: str
        :type rows: int
        :rtype: str
        """
        mx = []
        n = len(encodedText)
        i=0
        m = int(n/rows)
        while i<n:
            mx.append(encodedText[i:i+m])
            i+=m
        s = []
        c=0
        while c<m:
            nc, nr = c, 0
            while nc<m and nr<rows:
                s.append(mx[nr][nc])
                nr+=1
                nc+=1
            c+=1
        return "".join(s).rstrip()
        k = len(s)
        while k and s[k-1]==' ': k-=1
        return "".join(s[:k])

    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)
        columns = n // rows
        ans = []
        
        for i in range(columns):
            while (i < n):
                ans.append(encodedText[i])
                i += columns + 1
        
        return "".join(ans).rstrip()


s = Solution()
encodedText = "ch   ie   pr"
rows = 3
print(s.decodeCiphertext(encodedText, rows))