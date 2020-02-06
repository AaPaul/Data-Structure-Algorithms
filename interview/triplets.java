import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {


    // Complete the triplets function below.
    static long triplets(long t, List<Integer> d) {
        Collections.sort(d);
        long count = 0;
        System.out.println(d.size());
        System.out.println(t);
        // int i,j,k;
        // for (i=0, j=i+1, k=j+1;d.get(i) < (t/2) && i<d.size();) {
        //     if (d.get(j) >= (t/2)) {
        //         i++;
        //         j=i+1;
        //         k=j+1;
        //         continue;
        //     }
        //     if (k >= d.size()){
        //         j++;
        //         k = j+1;
        //     }
        //     if (k<d.size() && d.get(i)+d.get(j)+d.get(k) <= t){
        //             count++;
        //         }
        //     k++;
        //     System.out.println(k);
        // }




        // for (int i = 0; i < d.size() && d.get(i) < (t/2); i++){
        //     for (int j = i+1, k = j+1; j < d.size() && d.get(j) < (t/2); k++) {
        //         if (k >= d.size()){
        //             j++;
        //             k = j+1;
        //         }
        //         if (k<d.size() && d.get(i)+d.get(j)+d.get(k) <= t){
        //             count++;
        //         }
                
        //         // System.out.println("k"+k);
        //         // System.out.println("j"+j);
        //     }
        // }

        for (int i = 0; i < d.size() && d.get(i)<(t/3); i++){
            for (int j = i+1; j < d.size(); j++) {
                for (int k = j+1; k < d.size(); k++) {
                    if (d.get(i)+d.get(j)+d.get(k) <= t)
                        count++;
                    if (d.get(i)+d.get(j)+d.get(k) > t)
                        break;
                }
            }
        }
        return count;

    }
// 败在时间复杂度上，之后回头再总结

// compress string
// 遍历之后存入char数组，再次遍历，若是字母，将字母和数字存入hashmap（若为第一个则先继续遍历知道遇到第二个数字），若是数字，情况一：flag为0，将flag记为该数字，继续遍历；
// 情况二：flag不为0，flag=flag*10 + 该数字；继续遍历// 然后hashmap应该能将重复的部分存到一起，回头查找一下再进行记录
