// Longest Substring Without Repeating Characters
/**
*当我做这道题的时候，想了两种思路，然后进行第一种思路的时候被第二种思路误导，导致出现了maxNum持续增大的问题。第一种思路就是将不重复的字符保存到hashmap中，
*然后计算这个hashmap的size，若maxNum小于size，就update这个maxNum。若是遇到相同的字符，就清空map，从起始的第二个字符重新遍历。
*第二种思路就是每加一个字符到hashmap中，（maxNum增加1），用count计数，加一个字符就count+1，然后遇到重复字符，将count的值送给maxNum（count>maxNum），再从第二个遍历。
*其实第二种方法不需要hashmap也能进行，第一次选择第一种方法进行解答
*/

// The result is that this programe is too slow.
import java.util.HashMap;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Character> map = new HashMap<>();
        int maxNum = 0;
        for (int i = 0, tag = 0; i < s.length(); i++) {
            if(i == 0) {
                map.put(s.charAt(i), s.charAt(i));
                maxNum = 1;
            }
            else {
                if (map.containsKey(s.charAt(i))) {
                    map.clear();
                    // maxNum = 0;
                    tag++;
                    i = tag;
                }
                map.put(s.charAt(i), s.charAt(i));
                maxNum = (maxNum < map.size()) ? map.size() : maxNum;

            }
        }
        return maxNum;
    }
}


//程序中注释的部分是因为我没有考虑到新的count有可能会比之前保存的maxNum小，所以出错了。同样的，这个程序也运行很慢
import java.util.HashMap;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Character> map = new HashMap<>();
        int maxNum = 0;
        int count = 0;
        for (int i = 0, tag = 0; i < s.length(); i++) {
            if(i == 0) {
                map.put(s.charAt(i), s.charAt(i));
                maxNum = 1;
            }
            else {
                if (map.containsKey(s.charAt(i))) {
                    map.clear();
                    maxNum = (maxNum < count) ? count : maxNum;
                    // maxNum = count;
                    count = 0;
                    tag++;
                    i = tag;
                }
                map.put(s.charAt(i), s.charAt(i));
            }
            count ++;
        }
        maxNum = (maxNum < count) ? count : maxNum;
        return maxNum;
    }
}

// The official solution
public class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length(), ans = 0;
        // Here this solution makrs the sequence number which is the flag to decide whether the loop should restart from next character.
        Map<Character, Integer> map = new HashMap<>(); // current index of character
        // try to extend the range [i, j]
        for (int j = 0, i = 0; j < n; j++) {
            if (map.containsKey(s.charAt(j))) {
                i = Math.max(map.get(s.charAt(j)), i);
            }
            ans = Math.max(ans, j - i + 1);
            map.put(s.charAt(j), j + 1);
        }
        return ans;
    }
}
// The whole program just uses one hashmap while my onw ways create and clean hashmap again and again which is very time-consuming.
