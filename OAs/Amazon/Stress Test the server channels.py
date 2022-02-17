'''
https://leetcode.com/discuss/interview-question/1527667/amazon-oa-stress-test-the-server-channels

Eaxmple:- packets = [1,2,3,4,5] and channels = 2
One maximal solution is to transfer packets [1,2,3,4] through channel 1 and packet [5] through channel 2. The quality of transfer for channel 1 is (2+3)/2=2.5 and that of channel 2 is 5. Their sum is 2.5+5 =7.5 which is round up to 8.

Eaxmple:- packets = [2,2,1,5,3], channel = 2
One solution is to transfer packets [5] through one channel and packet [2,2,1,3] through other channel. the sum of quantity is 5+(2+2)/2=7

Eaxmple:- packets = [89,48,14], channel = 3
There are 3 channels for each 3 packets. Each channel carries one, so the overall sum of quantity is 89+48+14=151

Eaxmple:- packets = [1], channel = 1
There is onle one channel and only one packet so output is 1

'''

import statistics
import math

def serverhealth(arr, k):
    if k > len(arr):
        return False
    servers = 0
    arr.sort(reverse=True)
    servers += sum(arr[:k-1])
    return math.ceil(statistics.median(arr[k-1:]) + servers)

# print(serverhealth([89,48,14], 3))
print(serverhealth([2,2,1,5,3], 2))