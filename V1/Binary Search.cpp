#include <iostream>
#include <vector>

using namespace std;


class Solution {
public:
    int search(vector<int>& nums, int target) {
        
        int low = 0, high = nums.size()-1;

        while(low <= high){

            int mid = low + ((high-low)/2);

            if(nums[mid] == target){
                return mid;

            } else if(nums[mid] < target){
                low = mid+1;

            } else{
                high = mid-1;
            }
        }

        return -1;
    }
};

int main(){

    vector <int> Hola = {1,2,3,4,5};

    Solution Holis;

    cout << Holis.search(Hola,4);

    return 0;
}