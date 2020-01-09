// Solution 1

public class twoSum(int [] nums, int target) {
    for (int i = 0; i < nums.length; i++) {
        int temp = target - nums[i];
        for (int j = 0; j < nums.length; j++) {
            if (temp == nums[j] && j != i) {
                int [] conclusion = {i, j};
                return conclusion;
            }
        }
    }
    throw new IllegalArgumentException("No two sum solution");
}



// Solution 2
import java.util.HashMap;

public class twoSum(int [] nums, int target) {
    Map<Integer, Integer> map = new HashMap<>();
    for (int i = 0; i < nums.length; i++) {
        map.put(nums[i], i);
    }
    for (int i = 0; i < nums.length; i++) {
        int temp = target - nums[i];
        if (map.containsKey(temp) && map.get(temp) != i) {
            return new int[] {i, j};
        }
    }
    throw new IllegalArgumentException("No two sum solution");
}
