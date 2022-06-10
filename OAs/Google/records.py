def q1(s:list):
    ans = []
    ch_array = [chr(ord('a')+i) for i in range(26)]
    for w in s:
        temp = []
        temp.append(w)
        for ch in ch_array:
            if ch + w in s:
                temp.append(ch+w)
                