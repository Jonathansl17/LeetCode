#include <iostream>
using namespace std;

// Input: word1 = "abc", word2 = "pqr"
// Output: "apbqcr"
// Explanation: The merged string will be merged as so:
// word1:  a   b   c
// word2:    p   q   r
// merged: a p b q c r



class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string result = "";
        int maxLength = max(word1.length(), word2.length());

        for(int i = 0; i < maxLength; i++) {
            if(i < word1.length()) {
                result += word1[i];
            }
            if(i < word2.length()) {
                result += word2[i];
            }
        }

        return result;
    }
};


int main(){
    Solution Hola;

    string word1 = "abc";
    string word2 = "pqry";
    cout<<Hola.mergeAlternately(word1,word2);
}