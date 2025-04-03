#include <iostream>
using namespace std;

#include <vector>

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        
        int low = 0;
        int high = nums.size()-1;

        while (low <=high){
            int mid = low + ((high-low)/2);

            if(nums[mid] == target){
                return mid;

            } else if(nums[mid] < target){
                low = mid+1;

            } else{
                high = mid-1;
            }
        }
        return low;
    }

};


int main(){

    Solution Hola;

    vector<int> Lista= {1,3,5,6,7,8,9};

    cout << Hola.searchInsert(Lista,7);

    return 0;
}