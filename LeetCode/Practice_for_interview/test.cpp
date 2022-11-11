#include <iostream>
using namespace std;
int  main() {
    // vector<int> arr = {1, 6, 10, 16, 21, ...};
    // int l = 0, h = 5;
    // int k = 6
    // while (l < h) {
    //     int mid = l + (h - l) / 2;

    //     if (arr[mid] < k)
    //         l = mid + 1;
    //     else r = mid;
    // }
    // cout<<l<<endl;
    char** outtext12;
    fun(25, outtext12);
    return 0;
}

void fun(uint32_t in, char** outtext12) {
    vector<string> arr  = { "0" , "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "X" , "Y" };
    string res; 

	while(in)
	{
	    int x = in%12 ; 
        res += arr[x]; 
	    in = in/12 ; 
	}
    reverse(res.begin() , res.end());
    char* c_arr[] =
    outtext12 = const_cast<char *>(res.c_str());
}