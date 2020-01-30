/*
replace() doesn't support regular expressions
replaceAll & replaceFrist support.

Java String class has some functions like split which is same as the python version.
/*

class Solution {
    public String defangIPaddr(String address) {
        // String [] str = address.split("\\.");
        return address.replace(".", "[.]");
    }
}

// Java String class cannot be changed if it is be created

//StringBuffer is safer than StringBuild while the latter one is faster than the former one. Both of them can be modified after being created.

// This solution spend less than 1 ms to get the answer.
class Solution2 {
    public String defangIPaddr(String address) {
        // String [] str = address.split("\\.");
        char[] cr = address.toCharArray();
        StringBuilder sb= new StringBuilder(cr.length); //Note: dont need to add "()" to get the length of array.
        for (int i = 0; i < cr.length; i++) {
            if (cr[i] == '.') {
                sb.append("[.]");
            }
            else {
                sb.append(cr[i]);
            }
        }
        return sb.toString();
    }
}


//python3 
// string.join 是在每个字符后面添加该string，如果使用split函数将目标字符串分部分，就可以得到结果, 还可以在splite后添加[:-1]表示分割到最后一个部分前停止

/*
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return "[.]".join(address.split('.'))
*/
