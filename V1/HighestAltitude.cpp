#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int altitude = 0;
        int maxAltitude = 0;

        for(int i = 0; i < gain.size(); i++){
            altitude += gain[i];
            if (altitude > maxAltitude) {
                maxAltitude = altitude;
            }
        }

        return maxAltitude;
    }
};

int main() {
    Solution Hola;
    vector<int> Holaxd = {-5, 1, 5, 0, -7};

    cout << Hola.largestAltitude(Holaxd);
    
    return 0;
}