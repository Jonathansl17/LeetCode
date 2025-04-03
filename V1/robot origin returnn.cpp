#include <iostream>
using namespace std;

class Solution {
public:
    bool judgeCircle(string origin) {
        int ORIGIN[] = {0,0};

        for (char i : origin) {
            switch(i) {
                case 'U': ORIGIN[0]++; break;
                case 'D': ORIGIN[0]--; break;
                case 'L': ORIGIN[1]--; break;
                case 'R': ORIGIN[1]++; break; 
            }
        }
        return ORIGIN[0] == 0 && ORIGIN[1] == 0;
    }  
};


int main() {
    Solution obj;
    string movements = "UDLR";
    bool result = obj.judgeCircle(movements);
    if (result) {
        cout << "Regresa al origen." << endl;
    } else {
        cout << "No regresa al origen." << endl;
    }
    return 0;
}